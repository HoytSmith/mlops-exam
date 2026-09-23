# Hyperparameter Tuning Assessment

This project demonstrates a scalable hyperparameter tuning workflow for a machine learning model using Azure ML. The goal was to optimize a Random Forest model efficiently while following best practices for reproducibility, parallel execution, and model tracking.

## Overview

The project uses a tabular dataset to train and tune a Random Forest classifier. Instead of relying on a single-node approach such as scikit-learn GridSearchCV, the tuning process is designed to scale with Azure ML’s distributed execution capabilities.

This allows model selection to be run in parallel across multiple workers, which is more suitable for larger search spaces and more realistic production workflows.

## Objectives

The main goals of this project were to:

- train a Random Forest model on the provided diabetes dataset
- explore a defined hyperparameter grid
- optimize model performance using parallelized tuning
- compare candidate configurations efficiently
- register the best-performing model with MLflow
- demonstrate a production-style model tuning workflow in Azure ML

## Dataset

The project uses a structured tabular dataset containing medical features used to predict diabetes outcomes. The data is loaded and prepared for model training and validation before the tuning process begins.

## Model and Hyperparameter Search

A Random Forest model was selected for the experiment due to its robustness, interpretability, and wide use in structured data tasks.

The tuning process explores the following parameter grid:

- max_features: 3, 4, 5
- n_estimators: 100, 250

The search space was designed to evaluate how different feature subsets and tree counts affect model performance, while remaining scalable and suitable for parallel execution.

## Azure ML Workflow

The project uses Azure Machine Learning for distributed model tuning and experimentation. The workflow includes:

- creating or loading an Azure ML workspace
- preparing a training environment
- creating a tabular dataset reference
- launching a parallelized hyperparameter sweep
- monitoring job execution
- selecting the best-performing model
- registering the final model with MLflow

This approach reflects a realistic MLOps workflow where model experimentation is automated and tracked in a centralized platform.

## Model Registration and Tracking

The best model is registered using MLflow so it can be versioned and reused in downstream deployment or evaluation workflows. This is a core best practice in production ML pipelines, as it ensures model lineage, reproducibility, and traceability across experiments.

## Technologies Used

- Python
- scikit-learn
- Azure Machine Learning
- MLflow
- Azure Identity
- pandas
- numpy

## Skills Demonstrated

- machine learning model tuning
- distributed hyperparameter search
- Azure ML experimentation workflows
- model registration and versioning
- ML lifecycle best practices
- experiment tracking and reproducibility

## Outcome

This project showcases a scalable approach to model optimization beyond traditional local grid search. It highlights how Azure ML can be used to run parallelized tuning for machine learning models in a more production-ready and maintainable way.