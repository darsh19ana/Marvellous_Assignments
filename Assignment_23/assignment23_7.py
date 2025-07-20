from assignment23_1 import df
import numpy as np
import matplotlib.pyplot as plt

df['Total'] = df[['English', 'Math', 'Science']].sum(axis=1)

plt.bar(df['Name'], df['Total'])
plt.xlabel("student names")
plt.ylabel("total marks")
plt.title("students marks and names")

plt.show()