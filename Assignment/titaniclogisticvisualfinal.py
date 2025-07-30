import pandas as pd
import numpy as np

from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

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

    # figure()
    # target = "Survived"
    # sns.countplot(data = df, x = target).set_title("survived vs non survived")
    # show()

    # figure()
    # target = "Survived"
    # sns.countplot(data = df, x=target, hue = "Sex").set_title("Based on gender")
    # show()

    # figure()
    # target = "Survived"
    # sns.countplot(data = df, x=target, hue = "Pclass").set_title("Based on Pclass")
    # show()

    # figure()
    # df['Age'].plot.hist().set_title("Age report")
    # show()

    # figure()
    # df['Fare'].plot.hist().set_title("Fare report")
    # show()

    # plt.figure(figsize = (10, 6))
    # sns.heatmap(df.corr(), annot = True, cmap = "coolwarm")
    # plt.title("feature correlation heatmap")
    # plt.show()

    x = df.drop(columns = ["Survived"])
    y = df['Survived']

    print("dimensions of features: ", x.shape)
    print("dimesnions of labels: ", y.shape)

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size =0.2, random_state = 42)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    
    cm = confusion_matrix(y_test, y_pred)
    print("accuracy is: ", accuracy)
    print("confusion matrix: \n", cm)

def main():
    marvelloustitaniclogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()