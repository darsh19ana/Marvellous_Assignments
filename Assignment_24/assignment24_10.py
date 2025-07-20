import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finaldataset.csv")

plt.boxplot(df['English'])
plt.show()