# Machine Learning Assessment

This project contains two exploratory machine learning notebooks focused on model development, evaluation, and model explainability.

## Overview

The assessment covers two complementary tasks:

1. A classical machine learning workflow using a breast cancer dataset
2. A deep learning explainability workflow using Fashion-MNIST and SHAP

Together, these notebooks demonstrate how to prepare data, train models, evaluate performance, and interpret predictions.

The assessment also required a powerpoint presentation going over the project, aimed at fellow Data Scientists. This presentation is included in the project for those interested.

---

## Notebook 1: exam-ml.ipynb

This notebook explores a supervised classification problem using a breast cancer dataset stored in ARFF format.

### Objectives
- inspect and clean the dataset
- handle missing values
- encode target labels
- split data into training and test sets
- train and tune a Support Vector Classifier
- evaluate model performance using classification metrics
- identify the most important features

### Workflow
- Load the dataset and examine its structure
- Detect missing values and replace them with column means
- Encode the target variable to numeric values
- Train/test split with a fixed random seed
- Use GridSearchCV to tune hyperparameters for an SVC model
- Evaluate the model with accuracy, precision, recall, F1 score, and confusion matrix
- Visualize the model’s classification results
- Rank features by importance based on the learned coefficients

---

## Notebook 2: shap.ipynb

This notebook focuses on deep learning and model interpretability using Fashion-MNIST.

### Objectives
- load and preprocess the Fashion-MNIST dataset
- train a Convolutional Neural Network (CNN)
- visualize training progress
- use SHAP to explain model predictions
- explore how the model distinguishes between visually similar classes

### Workflow
- Download and reshape the Fashion-MNIST dataset
- Normalize pixel values for stable model training
- Build a CNN architecture with convolutional and pooling layers
- Train the model and track loss and accuracy
- Use SHAP’s DeepExplainer to compute feature attributions
- Visualize SHAP values for representative examples
- Interpret which image regions influence classification decisions

---

## Skills Demonstrated

- data cleaning and preprocessing
- feature engineering and encoding
- model training and hyperparameter tuning
- evaluation with classification metrics
- confusion matrix analysis
- deep learning with CNNs
- SHAP-based model explainability
- result interpretation and communication

## Outcome

This assessment demonstrates a strong foundation in both classical machine learning and deep learning explainability. It shows the ability to prepare data, train and tune models, evaluate results rigorously, and interpret model behavior in ways that support real-world decision-making. The combination of predictive modeling and explainability reflects a practical understanding of how machine learning systems should be evaluated, communicated, and trusted in professional settings.
