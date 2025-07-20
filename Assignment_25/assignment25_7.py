import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {'Age': [18, 22, 25, 30, 35]}
df = pd.DataFrame(data)

scaler = MinMaxScaler(feature_range=(0, 1)) # Default range is (0, 1)

scaled_data = scaler.fit_transform(df[['Age']])

print(scaled_data)