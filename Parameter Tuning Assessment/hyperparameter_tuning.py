"""
Script to train tune hyperparameters
Based on:
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-train-scikit-learn
"""

from azure.ai.ml import Input, command
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Model
from azure.ai.ml.sweep import Choice

from compute_aml import create_or_load_aml
from data_tabular import create_tabular_dataset, name_dataset
from environment import create_docker_environment, custom_env_name
from initialize_constants import AML_COMPUTE_NAME
from ml_client import create_or_load_ml_client

experiment_folder = "diabetes_hyperdrive"
experiment_name = "exam-param-tuning"
script_name = "diabetes_training.py"
registered_model_name = "diabetes_model_hyper"
best_model_name = "best_diabetes_model"


def main():
    # 1. Create or Load a ML client
    ml_client = create_or_load_ml_client()

    # 2. Create compute resources
    create_or_load_aml()

    # 3. Create and register a File Dataset
    create_tabular_dataset()
    latest_version_dataset = next(
        dataset.latest_version for dataset in ml_client.data.list() if dataset.name == name_dataset
    )

    # 4. Environment
    environment_names = [env.name for env in ml_client.environments.list()]
    if custom_env_name not in environment_names:
        create_docker_environment()

    # 5. Run Job
    job_for_sweep = command(
        inputs=dict(
            script_name=script_name,
            data=Input(
                type=AssetTypes.URI_FILE,
                # @latest doesn't work with dataset paths
                path=f"azureml:{name_dataset}:{latest_version_dataset}",
            ),
            registered_model_name=registered_model_name,
            max_features=Choice(values=[3, 4, 5]),
            n_estimators=Choice(values=[100, 250]),
        ),
        code=experiment_folder,
        command=(
            "python ${{inputs.script_name}}"
            + " --data ${{inputs.data}}"
            + " --registered_model_name ${{inputs.registered_model_name}}"
            + " --max_features ${{inputs.max_features}}"
            + " --n_estimators ${{inputs.n_estimators}}"
        ),
        environment=f"{custom_env_name}@latest",
        compute=AML_COMPUTE_NAME,
        experiment_name=experiment_name,
        display_name=experiment_name,
    )

    # Configure hyperdrive settings
    sweep_job = job_for_sweep.sweep(
        compute=AML_COMPUTE_NAME,
        sampling_algorithm="grid",
        primary_metric="AUC",
        goal="Maximize",
        max_total_trials=6,
        max_concurrent_trials=2,
    )

    # submit the command
    returned_sweep_job = ml_client.create_or_update(sweep_job)

    # stream the output and wait until the job is finished
    ml_client.jobs.stream(returned_sweep_job.name)

    # refresh the latest status of the job after streaming
    returned_sweep_job = ml_client.jobs.get(name=returned_sweep_job.name)

    # Find and register the best model
    if returned_sweep_job.status == "Completed":
        # First let us get the run which gave us the best result
        best_run = returned_sweep_job.properties["best_child_run_id"]

        # lets get the model from this run
        model = Model(
            # the script stores the model as the given name
            path=(f"azureml://jobs/{best_run}/outputs/artifacts/paths/{registered_model_name}/"),
            name=best_model_name,
            type="mlflow_model",
        )
    else:
        print(
            f"Sweep job status: {returned_sweep_job.status}. \
                Please wait until it completes"
        )

    # Register best model
    print(f"Registering Model {best_model_name}")
    ml_client.models.create_or_update(model=model)


if __name__ == "__main__":
    main()
