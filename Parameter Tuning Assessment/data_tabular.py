"""
Script to create and register file as an uri
"""

from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Data

from ml_client import create_or_load_ml_client

name_dataset = "diabetes"
data_folder = "./data/diabetes.csv"


def create_tabular_dataset():
    # 1. Create or Load a ML client
    ml_client = create_or_load_ml_client()

    # 2. Add files
    if name_dataset not in [dataset.name for dataset in ml_client.data.list()]:
        tab_data_set = Data(
            path=data_folder,
            type=AssetTypes.URI_FILE,
            name=name_dataset,
        )

        ml_client.data.create_or_update(tab_data_set)
    else:
        print("Dataset already registered.")


if __name__ == "__main__":
    create_tabular_dataset()
