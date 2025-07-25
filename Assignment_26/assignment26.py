import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("PlayPredictor.csv")
print(df.head())
df = df.drop(columns=['Unnamed: 0'])

print("Missing  values: ", df.isnull().sum())

le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

x = df.drop(columns = ["Play"], axis = 1)
y = df["Play"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = KNeighborsClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy is: ", accuracy)



