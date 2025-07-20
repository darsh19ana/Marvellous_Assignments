import pandas as pd

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
    'Gender': ['Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=False)

print(df_encoded)