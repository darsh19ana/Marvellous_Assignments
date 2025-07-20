from assignment23_1 import df

print("original dataset: \n", df.head())

df = df.drop('English', axis=1)

print("dataset updated: \n", df.head())