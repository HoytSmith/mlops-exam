"""
Script to create and register an environment including SKlearn
"""

import os

from azure.ai.ml.entities import Environment

from ml_client import create_or_load_ml_client

dependencies_dir = "./dependencies"
custom_env_name = "custom-scikit-learn"


def create_docker_environment():
    # 1. Create or Load a ML client
    ml_client = create_or_load_ml_client()

    # 2. Create a Python environment for the experiment
    env_docker_image = Environment(
        name=custom_env_name,
        conda_file=os.path.join(dependencies_dir, "conda.yml"),
        image="mcr.microsoft.com/azureml/openmpi5.0-ubuntu24.04:latest",
    )
    ml_client.environments.create_or_update(env_docker_image)

    print(
        f"Environment with name {env_docker_image.name} is registered to the workspace,",
        f"the environment version is {env_docker_image.version}",
    )


if __name__ == "__main__":
    create_docker_environment()
