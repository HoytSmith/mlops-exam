"""
Script to initialize MLClient object
"""

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

from initialize_constants import AZURE_RESOURCE_GROUP, AZURE_SUBSCRIPTION_ID, AZURE_WORKSPACE_NAME


def create_or_load_ml_client():
    """Create or load an Azure ML Client based on env variables.
    Args:
        None since information is taken from global constants
            defined in initialize_constants.py.

    Returns:
        A workspace and set quick load.
    """
    try:
        credential = DefaultAzureCredential()
        # Check if given credential can get token successfully.
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:
        # Fall back to InteractiveBrowserCredential
        # in case DefaultAzureCredential not working
        print(ex)
        credential = InteractiveBrowserCredential()

    # Get a handle to the workspace.
    # You can find the info on the workspace tab on ml.azure.com
    ml_client = MLClient(
        credential=credential,
        subscription_id=AZURE_SUBSCRIPTION_ID,
        resource_group_name=AZURE_RESOURCE_GROUP,
        workspace_name=AZURE_WORKSPACE_NAME,
    )
    return ml_client


if __name__ == "__main__":
    ml_client = create_or_load_ml_client()
    print(ml_client)
