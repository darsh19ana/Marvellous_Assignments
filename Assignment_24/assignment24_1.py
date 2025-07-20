# normalize the 'Math' scores using minmax scaling

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler to the data and transform it
normalized_data = scaler.fit_transform((df[['Math']]))

print("normalized math: ", normalized_data)
