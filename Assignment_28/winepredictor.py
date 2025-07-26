import pandas as pd
import numpy as np

from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix

def winepredictor(datapath):
    df = pd.read_csv(datapath)

    print("dataset loadeed sucessfully")
    print(df.head())

    print("dimensions of dataset are: ", df.shape)

    print("missing values: ",df.isnull().sum())

    x = df.drop(columns = ["Class"])
    y = df['Class']

    print("dimensions of features: ", x.shape)
    print("dimesnions of labels: ", y.shape)

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size =0.2, random_state = 42)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    
    cm = confusion_matrix(y_test, y_pred)
    print("accuracy is: ", accuracy)
    print("confusion matrix: \n", cm)

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    
    cm = confusion_matrix(y_test, y_pred)
    print("accuracy is: ", accuracy)
    print("confusion matrix: \n", cm)

def main():
    winepredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()