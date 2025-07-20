import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finaldataset.csv")

df = df.rename(columns={'Math': 'Mathematics'})
print(df)