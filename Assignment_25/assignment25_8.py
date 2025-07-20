import pandas as pd
import numpy as np

data = {'Marks': [85, np.nan, 90, np.nan, 95]}
df = pd.DataFrame(data)

df = df.interpolate()
print(df)