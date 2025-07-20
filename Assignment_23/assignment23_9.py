# 

import pandas as pd
import numpy as np

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science':[91, np.nan, 85]
}

df = pd.DataFrame(data2)

print(df.isnull().sum())

df[['Math', 'Science']] = df[['Math', 'Science']].fillna(df[['Math', 'Science']].mean())

print(df.head())