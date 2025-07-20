from assignment24_1 import df
import pandas as pd

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
    'Gender': ['Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

dataset = df.to_csv("finaldataset.csv")
print("csv saved")