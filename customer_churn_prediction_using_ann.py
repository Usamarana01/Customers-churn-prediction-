# -*- coding: utf-8 -*-
"""Customer Churn prediction Using ANN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gIOyq_Ts8-GEVisy1x6VJ8IQhOnVdMvH

# Customer Churn Prediction Using Artificial Neural Networks (ANN)

This notebook demonstrates how to use Artificial Neural Networks (ANNs) to predict customer churn. Customer churn refers to the phenomenon where customers stop doing business with a company. Predicting churn is essential for businesses as it allows them to identify customers at risk of leaving and take proactive measures to retain them.

In this notebook, we'll follow these steps:
1. **Data Loading and Exploration**: Load the dataset and explore its features and distribution.
2. **Data Preprocessing**: Prepare the data for training by handling missing values, encoding categorical variables, and scaling numerical features.
3. **Model Building**: Construct an ANN model using TensorFlow and Keras.
4. **Model Training**: Train the ANN model on the training data.
5. **Model Evaluation**: Evaluate the performance of the trained model on the test data using metrics such as accuracy and confusion matrix.
6. **Conclusion**: Summarize the findings and discuss potential next steps for improving the model.

Let's dive in!
"""

import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""# DataSet
using "**Telco-Customer-Churn**" from kaggle
"""

df=pd.read_csv("Telco-Customer-Churn.csv")
df

df.dtypes

df.drop('customerID' , axis='columns' , inplace=True )

pd.to_numeric(df.TotalCharges , errors='coerce').isnull()

df[pd.to_numeric(df.TotalCharges , errors='coerce').isnull()]

df1=df[df.TotalCharges!=' ']
df1.shape
df1

df1.TotalCharges=pd.to_numeric(df1.TotalCharges , errors='coerce')

gender_churn = df1.groupby(['gender', 'Churn']).size().unstack()

# Plotting
gender_churn.plot(kind='bar', stacked=True)
plt.title('Churn Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

churned_customers_yes = df[df['Churn'] == 'Yes'].tenure
churned_customers_no = df[df['Churn'] == 'No'].tenure
plt.hist([churned_customers_yes, churned_customers_no], color=['green', 'red'], label=['Churn=yes', 'Churn=no'])
plt.xlabel("Tenure")
plt.ylabel("Number of customers")
plt.title("Customer Churn Prediction")
plt.legend()
plt.show()

churned_customers_yes = df[df['Churn'] == 'Yes'].MonthlyCharges
churned_customers_no = df[df['Churn'] == 'No'].MonthlyCharges
plt.hist([churned_customers_yes, churned_customers_no], color=['green', 'red'], label=['Churn=yes', 'Churn=no'])
plt.xlabel("Monthly Charges")
plt.ylabel("Number of customers")
plt.title("Customer Churn Prediction")
plt.legend()
plt.show()

"""## Label Encoding and Data Cleaning

Before training our model, it's essential to preprocess the data. This involves handling any missing values, encoding categorical variables, and ensuring all features are in a suitable format for the model.

### Handling Missing Values

First, we'll check for any missing values in the dataset and handle them appropriately. This ensures that our model can learn from the complete dataset without being affected by missing data.

### Label Encoding

Many machine learning algorithms, including neural networks, require numerical input. Therefore, we'll encode categorical variables into numerical format using label encoding. This transformation ensures that categorical variables can be used as input features for the model.

### Data Cleaning

In addition to handling missing values and encoding categorical variables, we'll perform any necessary data cleaning steps. This may include removing unnecessary columns, standardizing data formats, or handling outliers.

Let's proceed with these preprocessing steps to prepare our data for training the neural network.

"""

def unique_value(df):
  for column in df:
    if df[column].dtypes == 'object':
      print(f'{column}:{df[column].unique()}')

unique_value(df1)

df1.replace('No internet service','No',inplace=True)
df1.replace('No phone service','No',inplace=True)
unique_value(df1)

columns_to_modify = ['Partner','PaperlessBilling','Dependents','PhoneService','MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for col in columns_to_modify:
    if df1[col].dtype == 'object':
        df1[col].replace({'Yes': 1, 'No': 0}, inplace=True)

print(df1.columns)

df1['gender'].replace({"Male":1,"Female":0},inplace=True)

columns_to_encode = ['InternetService', 'Contract', 'PaymentMethod']

df1 = pd.get_dummies(data=df1, columns=columns_to_encode)

df1.dtypes

column_scale=['tenure','MonthlyCharges','TotalCharges']
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df1[column_scale] = scaler.fit_transform(df1[column_scale])

"""**Train test Split**"""

X = df1.drop('Churn', axis=1)
y = df1['Churn']

# Use LabelEncoder to convert 'Churn' column to numerical labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

X_train.isnull().sum()
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

X_train.dtypes

"""# prompt: write markdown for model

# **Model Building**

Now that we have preprocessed our data, we can start building our ANN model. We'll use TensorFlow and Keras to construct a multi-layer neural network for predicting customer churn.

**Model Architecture:**

Our model will consist of the following layers:

- Input layer: Accepts the preprocessed features from the data.
- Hidden layers: We'll use multiple hidden layers with varying sizes to learn complex patterns in the data.
- Output layer: Produces a single output node representing the predicted churn probability (between 0 and 1).

**Activation Functions:**

- We'll use the `relu` activation function for the hidden layers.
- The output layer will use the `sigmoid` activation function to provide a probability score between 0 and 1.

**Loss Function and Optimizer:**

- We'll use the `binary_crossentropy` loss function to measure the model's performance.
- The `adam` optimizer will be used to update the model's weights during training.

**Metrics:**

- We'll track the model's performance using the `accuracy` metric, which measures the percentage of correctly predicted churn cases.

**Training:**

- The model will be trained for a specified number of epochs (iterations) using the training data.
- During training, the model will learn to adjust its weights to minimize the loss function.

**Evaluation:**

- After training, the model will be evaluated on the test data to assess its ability to predict churn.
- We'll use the `accuracy` metric to evaluate the model's performance on the test data.

By following these steps, we can build a robust ANN model for predicting customer churn.
"""

model = keras.models.Sequential([
    keras.layers.Dense(20, input_shape=(X_train.shape[1],), activation='relu'),
    keras.layers.Dense(15, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100)

model.evaluate(X_test , y_test)

yp=model.predict(X_test)
 yp[:5]

y_pred = []
for element in yp:
    if element > 0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)

y_pred[:10]

y_pred[:10]

"""**Confusion Matrix**"""

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion Matrix")
plt.show()
