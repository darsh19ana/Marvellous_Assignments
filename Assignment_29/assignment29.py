import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("diabetes.csv")

# EDA
print("First five columns:",df.head())
print("Information about the columns: ",df.info)
print("Basic stats: ",df.describe())

print("Checking for null values: ",df.isnull().sum())

# # Plot the distribution of the target variable (Outcome)
# df['Outcome'].value_counts().plot(kind='bar', color=['skyblue', 'pink'])
# plt.title('Distribution of Outcome Variable')
# plt.xlabel('Outcome')
# plt.ylabel('Count')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

# # Plot histogram for each numerical column
# df.hist(bins=20, figsize=(10, 6), color='lightblue', edgecolor='black')
# plt.suptitle('Histograms of Features')
# plt.tight_layout()
# plt.show()

# # Plot boxplots for all features
# plt.figure(figsize=(10, 6))
# for i, column in enumerate(df.columns[:-1], 1): 
#     plt.subplot(3, 3, i)
#     sns.boxplot(y=df[column], color='lightgreen')
#     plt.title(f'Boxplot of {column}')
# plt.tight_layout()
# plt.show()

# # Pairplot colored by Outcome
# sns.pairplot(df, hue='Outcome', diag_kind='hist', palette='Set1')
# plt.suptitle('Pairplot of Features Colored by Outcome')
# plt.show()

# data preprocessing

x = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy with logistic regression is: ", accuracy)

cm = confusion_matrix(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision with logistic regression: ", prec)
print("Recall with logistic regression:", rec)
print("F1 Score with logistic regression:", f1)
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
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision with knn: ", prec)
print("Recall with knn:", rec)
print("F1 Score with knn:", f1)
print("Confusion Matrix with knn:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy with decision tree is: ", accuracy)

cm = confusion_matrix(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision with decision tree: ", prec)
print("Recall with decision tree:", rec)
print("F1 Score with decision tree:", f1)
print("Confusion Matrix with decision tree:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Convert to DataFrame for display and saving
# considering predictions using decision tree(best accuracy)
predictions_df = pd.DataFrame({
    "Actual Outcome": y_test.values,
    "Predicted Outcome": y_pred
})

print(predictions_df.head(10))

predictions_df.to_csv("diabetes_predictions.csv", index=False)
print("Predictions saved to 'diabetes_predictions.csv'")

