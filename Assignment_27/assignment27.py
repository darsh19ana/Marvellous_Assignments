import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Advertising.csv")
print(df.head())
df = df.drop(columns=['Unnamed: 0'])

print("Missing  values: ", df.isnull().sum())

le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

x = df.drop(columns = ["sales"], axis = 1)
y = df["sales"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)

# Display predicted values of Linear regression algorithms as well as expected values 
# which are provided by the data set.
comparison_df = pd.DataFrame({
    'Actual Sales': y_test.values,
    'Predicted Sales': y_pred
})

print(comparison_df.head())

