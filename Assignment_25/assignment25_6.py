import pandas as pd

data = {'Grade':['A+', 'B', 'A', 'C', 'B+']}
df = pd.DataFrame(data)

df = df.replace('A+', 'Excellent')
df = df.replace('A', 'Very Good')
df = df.replace('B+', 'Good')
df = df.replace('B', 'Average')
df = df.replace('C', 'Poor')

print(df)