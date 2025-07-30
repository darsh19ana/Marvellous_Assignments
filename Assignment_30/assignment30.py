import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("bank-full.csv", sep=';')

# EDA
print("First five columns:\n",df.head())
print("Information about the columns: ",df.info)
print("Basic stats: ",df.describe())
print("Class distribution: ",df['y'].value_counts())

# Plot class distribution
sns.countplot(x='y', data=df, palette='Set2')
plt.title('Class Distribution of Term Deposit Subscription')
plt.xlabel('Subscribed to Term Deposit')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--')
plt.show()

print(df['y'].unique())

print("Checking for null values: ",df.isnull().sum())

print("Data Types of columns: ",df.dtypes)

df_encoded = pd.get_dummies(df.drop('y', axis=1), drop_first=True)

df_encoded['y'] = df['y'].map({'yes': 1, 'no': 0})

x = df_encoded.drop('y', axis=1)
y = df_encoded['y']

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy with logistic regression is: ", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix with logistic regression:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

model = KNeighborsClassifier(n_neighbors=7)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy with knn is: ", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix with knn:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy with decision tree is: ", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix with random forest:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()