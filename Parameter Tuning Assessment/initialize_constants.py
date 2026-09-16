"""
Script to initialize global constants
"""

import os

# Global constants can be set via environmental variables
# Remove default values in production
AZURE_RESOURCE_GROUP = os.getenv("AZURE_RESOURCE_GROUP", "itvitae-exam")
AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID", "34faeead-244d-4ae8-8194-1eeaaffaf5be")
AZURE_WORKSPACE_NAME = os.getenv(
    "AZURE_WORKSPACE_NAME",
    "ws-Hoyt-Smith",
)
AZURE_LOCATION = os.getenv("AZURE_LOCATION", "westeurope")
# Choose names for your clusters
AML_COMPUTE_NAME = os.getenv("AML_COMPUTE_NAME", "aml-compute")
# General Servers Characteristics
VM_SIZE = os.getenv("VM_SIZE", "STANDARD_DS2_V2")
MIN_NODES = int(os.getenv("MIN_NODES", 0))
MAX_NODES = int(os.getenv("MAX_NODES", 1))
AGENT_COUNT = int(os.getenv("AGENT_COUNT", 2))
