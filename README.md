# Customer Churn Prediction Using Artificial Neural Networks (ANN)

This project aims to predict customer churn using Artificial Neural Networks (ANNs). Customer churn, also known as customer attrition, refers to the phenomenon where customers stop doing business with a company. Predicting churn is crucial for businesses as it allows them to identify customers at risk of leaving and take proactive measures to retain them.

## Dataset

The dataset used for this project is the "Telco-Customer-Churn" dataset, obtained from Kaggle. It contains various features related to customer demographics, services, and churn status.

## Overview

This notebook follows the following steps:
1. **Data Loading and Exploration**: Load the dataset and explore its features and distribution.
2. **Data Preprocessing**: Prepare the data for training by handling missing values, encoding categorical variables, and scaling numerical features.
3. **Model Building**: Construct an ANN model using TensorFlow and Keras.
4. **Model Training**: Train the ANN model on the training data.
5. **Model Evaluation**: Evaluate the performance of the trained model on the test data using metrics such as accuracy and confusion matrix.

## Label Encoding and Data Cleaning

Before training the model, the data undergoes preprocessing:
- **Handling Missing Values**: Missing values are identified and handled appropriately.
- **Label Encoding**: Categorical variables are encoded into numerical format using label encoding.
- **Data Cleaning**: Any necessary data cleaning steps, such as removing unnecessary columns or standardizing data formats, are performed.

## Model Building

The ANN model architecture consists of multiple layers, including input, hidden, and output layers. The model is trained using the Adam optimizer and binary cross-entropy loss function. The accuracy metric is used to evaluate the model's performance.

## Conclusion

By following these steps, we can build a robust ANN model for predicting customer churn, which can help businesses identify and retain at-risk customers.

For a detailed implementation, please refer to the provided notebook.
