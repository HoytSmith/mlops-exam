# Machine Learning Assessment

This project contains two exploratory machine learning workflows focused on model development, evaluation, and explainability. Together, they highlight my ability to work across both classical machine learning and modern deep learning practices while keeping the analysis grounded in real-world interpretation and business relevance.

## Overview

The assessment covers two complementary tasks:

1. A classical machine learning workflow using a breast cancer dataset
2. A deep learning explainability workflow using Fashion-MNIST and SHAP

Together, these notebooks demonstrate how to prepare data, train models, evaluate performance, and interpret predictions in a way that supports decision-making and trust in model outputs.

The assessment also required a powerpoint presentation for fellow Data Scientists, and this project includes the presentation for those interested.

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

- load the dataset and examine its structure
- detect missing values and replace them with column means
- encode the target variable to numeric values
- perform a train/test split with a fixed random seed
- use GridSearchCV to tune hyperparameters for an SVC model
- evaluate the model with accuracy, precision, recall, F1 score, and confusion matrix
- visualize the model’s classification results
- rank features by importance based on the learned coefficients

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

- download and reshape the Fashion-MNIST dataset
- normalize pixel values for stable model training
- build a CNN architecture with convolutional and pooling layers
- train the model and track loss and accuracy
- use SHAP’s DeepExplainer to compute feature attributions
- visualize SHAP values for representative examples
- interpret which image regions influence classification decisions

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
