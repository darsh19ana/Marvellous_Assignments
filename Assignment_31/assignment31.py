import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve, ConfusionMatrixDisplay, RocCurveDisplay
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

df['target'] = data.target

print("first 5 rows: ", df.head())
print("columns:",df.columns)
print("basic stats: ", df.describe())
print("Checking for null values: ",df.isnull().sum())
print("Data Types of columns: ",df.dtypes)

x = df.drop(columns='target') 
y = df['target']  

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier()
gb_model = GradientBoostingClassifier()

dt_model.fit(x_train, y_train)
rf_model.fit(x_train, y_train)
gb_model.fit(x_train, y_train)

dt_pred = dt_model.predict(x_test)
rf_pred = rf_model.predict(x_test)
gb_pred = gb_model.predict(x_test)

# accuracy scores
dt_acc = accuracy_score(y_test, dt_pred)
rf_acc = accuracy_score(y_test, rf_pred)
gb_acc = accuracy_score(y_test, gb_pred)

print(f"Decision Tree Accuracy: {dt_acc:.2f}")
print(f"Random Forest Accuracy: {rf_acc:.2f}")
print(f"Gradient Boosting Accuracy: {gb_acc:.2f}")

# predict probabilities
dt_prob = dt_model.predict_proba(x_test)[:, 1]
rf_prob = rf_model.predict_proba(x_test)[:, 1]
gb_prob = gb_model.predict_proba(x_test)[:, 1]

dt_fpr, dt_tpr, dt_thresholds = roc_curve(y_test, dt_prob)
rf_fpr, rf_tpr, rf_thresholds = roc_curve(y_test, rf_prob)
gb_fpr, gb_tpr, gb_thresholds = roc_curve(y_test, gb_prob)

dt_auc_score = roc_auc_score(y_test, dt_prob)
print(f"Decision Tree ROC AUC Score: {dt_auc_score:.2f}")

rf_auc_score = roc_auc_score(y_test, rf_prob)
print(f"Random Forest ROC AUC Score: {rf_auc_score:.2f}")

gb_auc_score = roc_auc_score(y_test, gb_prob)
print(f"Gradient Boosting ROC AUC Score: {gb_auc_score:.2f}")

# ROC Curve Plot 
plt.figure(figsize=(8,6))
plt.plot(dt_fpr, dt_tpr, label=f'Decision Tree (AUC = {dt_auc_score:.2f})', color='blue')
plt.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {rf_auc_score:.2f})', color='green')
plt.plot(gb_fpr, gb_tpr, label=f'Gradient Boosting (AUC = {gb_auc_score:.2f})', color='red')
plt.plot([0, 1], [0, 1], 'k--') 
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend(loc='lower right')
plt.grid()
plt.show()

# Confusion Matrices
models = {
    "Decision Tree": dt_pred,
    "Random Forest": rf_pred,
    "Gradient Boosting": gb_pred
}

for name, preds in models.items():
    cm = confusion_matrix(y_test, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
    disp.plot()
    plt.title(f"{name} - Confusion Matrix")
    plt.grid(False)
    plt.show()

# Bar Plot to Compare Accuracy & AUC Scores
model_names = ['Decision Tree', 'Random Forest', 'Gradient Boosting']
accuracies = [dt_acc, rf_acc, gb_acc]
auc_scores = [dt_auc_score, rf_auc_score, gb_auc_score]

x = np.arange(len(model_names))
width = 0.35

plt.figure(figsize=(9, 5))
plt.bar(x - width/2, accuracies, width, label='Accuracy', color='skyblue')
plt.bar(x + width/2, auc_scores, width, label='ROC AUC Score', color='pink')
plt.xticks(x, model_names)
plt.ylim(0.8, 1.0)
plt.ylabel("Score")
plt.title("Model Comparison: Accuracy vs. ROC AUC")
plt.legend()
plt.grid(axis='y')
plt.show()


