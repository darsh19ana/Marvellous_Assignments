import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, ConfusionMatrixDisplay
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

df1 = pd.read_csv("Fake.csv")
df2 = pd.read_csv("True.csv")

print(df1.isnull().sum())
print(df2.isnull().sum())

df1 = df1.drop(columns = ["subject", "date"])
print(df1.head())

df2 = df2.drop(columns = ["subject", "date"])
print(df2.head())

df1["target"] = 0 
df2["target"] = 1

# Combine both datasets
df = pd.concat([df1, df2], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
print(df["target"].value_counts())

df["combined_text"] = df["title"] + df["text"]
x = df["combined_text"]
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

tfidf = TfidfVectorizer(stop_words='english', max_features=5000)

x_train_tfidf = tfidf.fit_transform(x_train)
x_test_tfidf = tfidf.transform(x_test)

log_model = LogisticRegression()
log_model.fit(x_train_tfidf, y_train)

y_pred = log_model.predict(x_test_tfidf)

accuracy_log = accuracy_score(y_test, y_pred)
print("accuracy with logistic regression is: ", accuracy_log)

cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "True"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix: Logistic Regression")
plt.grid(False)
plt.show()

dt_model = DecisionTreeClassifier(max_depth=7)
dt_model.fit(x_train_tfidf, y_train)

y_pred = dt_model.predict(x_test_tfidf)

accuracy_dt = accuracy_score(y_test, y_pred)
print("accuracy with decision tree is: ", accuracy_dt)

cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "True"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix: Decision Tree")
plt.grid(False)
plt.show()

# hard voting
voting_hard = VotingClassifier(estimators=[
    ('lr', log_model), 
    ('dt', dt_model)
], voting='hard')

voting_hard.fit(x_train_tfidf, y_train)
y_pred_hard = voting_hard.predict(x_test_tfidf)

acc_hard = accuracy_score(y_test, y_pred_hard)
print("accuracy with hard voting:", acc_hard)

cm = confusion_matrix(y_test, y_pred_hard)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "True"])
disp.plot(cmap="Purples")
plt.title("Confusion Matrix: Hard Voting")
plt.grid(False)
plt.show()