"""
Script to initialize an Azure Machine Learning compute cluster (aml)
"""

from azure.ai.ml.entities import AmlCompute

from initialize_constants import AML_COMPUTE_NAME, MAX_NODES, MIN_NODES, VM_SIZE
from ml_client import create_or_load_ml_client


def create_or_load_aml(
    cpu_compute_target=AML_COMPUTE_NAME,
    vm_size=VM_SIZE,
    min_nodes=MIN_NODES,
    max_nodes=MAX_NODES,
):
    """Create or load an Azure Machine Learning compute cluster (aml) in a
        given Workspace.
    Args:
        cpu_compute_target: Name of the compute resource
        vm_size: Virtual machine size, VM_SIZE is used as default,
            for example STANDARD_D2_V2. Set to STANDARD_NC6 to get a GPU
        min_nodes: Minimal number of nodes, MIN_NODES is used as default.
        max_nodes: Minimal number of nodes, MIN_NODES is used as default.

    Returns:
        An aml and set quick load.
    """
    # Create or Load a Workspace
    ml_client = create_or_load_ml_client()
    try:
        # let's see if the compute target already exists
        cpu_cluster = ml_client.compute.get(AML_COMPUTE_NAME)
        print(
            f"You already have a cluster named {AML_COMPUTE_NAME},",
            "we'll reuse it.",
        )
    except Exception:
        print("Creating a new cpu compute target...")
        cpu_cluster = AmlCompute(
            name=cpu_compute_target,
            # Azure ML Compute is the on-demand VM service
            type="amlcompute",
            # VM Family
            size=vm_size,
            # Minimum running nodes when there is no job running
            min_instances=min_nodes,
            # Nodes in cluster
            max_instances=max_nodes,
            # How many seconds will the node running after the job termination
            idle_time_before_scale_down=180,
            # Dedicated or LowPriority.
            # The latter is cheaper but there is a chance of job termination
            tier="Dedicated",
        )

        # Now, we pass the object to MLClient's create_or_update method
        cpu_cluster = ml_client.compute.begin_create_or_update(AML_COMPUTE_NAME)

    return cpu_cluster


if __name__ == "__main__":
    create_or_load_aml()
