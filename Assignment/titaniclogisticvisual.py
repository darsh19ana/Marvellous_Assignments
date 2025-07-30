import pandas as pd
import numpy as np

from matplotlib.pyplot import figure, show
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, confusion_matrix

def marvelloustitaniclogistic(datapath):
    df = pd.read_csv(datapath)

    print("dataset loadeed sucessfully")
    print(df.head())

    print("dimensions of dataset are: ", df.shape)

    df.drop(columns = ['Passengerid', 'zero'], inplace = True)

    print("dimension: ", df.shape)

    print("missing values: ",df.isnull().sum())
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace = True)

    figure()
    target = "Survived"
    sns.countplot(data = df, x = target).set_title("survived vs non survived")
    show()

    figure()
    target = "Survived"
    sns.countplot(data = df, x=target, hue = "Sex").set_title("Based on gender")
    show()

    figure()
    target = "Survived"
    sns.countplot(data = df, x=target, hue = "Pclass").set_title("Based on Pclass")
    show()

    figure()
    df['Age'].plot.hist().set_title("Age report")
    show()

    figure()
    df['Fare'].plot.hist().set_title("Fare report")
    show()

def main():
    marvelloustitaniclogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()