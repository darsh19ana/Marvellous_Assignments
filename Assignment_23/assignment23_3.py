# add a column 'total' to the dataframe as the sum of all subject marks

from assignment23_1 import df

df['Total'] = df[['English', 'Math', 'Science']].sum(axis=1)

print(df.head())