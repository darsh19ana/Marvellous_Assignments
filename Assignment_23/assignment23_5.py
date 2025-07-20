# replace 'pooja' with 'puja' in 'Name' column

from assignment23_1 import df

df['Name'].replace('Pooja', 'Puja', inplace = True)

print(df.head())