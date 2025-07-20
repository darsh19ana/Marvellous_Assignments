import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = {'City':['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()
encoded_data = label_encoder.fit_transform(df)

print(encoded_data)