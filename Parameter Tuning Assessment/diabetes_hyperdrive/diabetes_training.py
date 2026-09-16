# Import libraries
import argparse
import os

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def main():
    """Main function of the script."""

    # Input and output arguments

    # Get script arguments
    parser = argparse.ArgumentParser()

    # Input dataset
    parser.add_argument(
        "--data",
        type=str,
        help="path to input data",
    )

    # Model name
    parser.add_argument("--registered_model_name", type=str, help="model name")

    # Hyperparameters
    parser.add_argument(
        "--max_features",
        type=int,
        dest="max_features",
        default=3,
        help="maximum number of features to consider when looking for the best split",
    )
    parser.add_argument(
        "--n_estimators",
        type=int,
        dest="n_estimators",
        default=100,
        help="number of trees in the forest",
    )

    # Add arguments to args collection
    args = parser.parse_args()
    print(" ".join(f"{k}={v}" for k, v in vars(args).items()))

    # Start Logging
    mlflow.start_run()

    # enable autologging
    mlflow.sklearn.autolog()

    # load the diabetes data (passed as an input dataset)
    print("input data:", args.data)

    diabetes = pd.read_csv(args.data)

    # Separate features and labels
    X, y = (
        diabetes[
            [
                "Pregnancies",
                "PlasmaGlucose",
                "DiastolicBloodPressure",
                "TricepsThickness",
                "SerumInsulin",
                "BMI",
                "DiabetesPedigree",
                "Age",
            ]
        ].values,
        diabetes["Diabetic"].values,
    )

    # Split data into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # Train a Random Forest classification model
    # with the specified hyperparameters
    print("Training a Random Forest classification model")
    model = RandomForestClassifier(
        max_features=args.max_features,
        n_estimators=args.n_estimators,
        random_state=0,
    ).fit(X_train, y_train)

    # calculate accuracy
    y_hat = model.predict(X_test)
    accuracy = np.average(y_hat == y_test)
    print("Accuracy:", accuracy)
    mlflow.log_metric("Accuracy", float(accuracy))

    # calculate AUC
    y_scores = model.predict_proba(X_test)
    auc = roc_auc_score(y_test, y_scores[:, 1])
    print("AUC: " + str(auc))
    mlflow.log_metric("AUC", float(auc))

    # Registering the model to the workspace
    print("Registering the model via MLFlow")
    mlflow.sklearn.log_model(
        sk_model=model,
        registered_model_name=args.registered_model_name,
        artifact_path=args.registered_model_name,
    )

    # Saving the model to a file
    mlflow.sklearn.save_model(
        sk_model=model,
        path=os.path.join(args.registered_model_name, "trained_model"),
    )

    # Stop Logging
    mlflow.end_run()


if __name__ == "__main__":
    main()
