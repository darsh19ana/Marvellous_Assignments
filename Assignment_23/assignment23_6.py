# sort the dataframe by descending order by 'Total' marks

from assignment23_1 import df

df['Total'] = df[['English', 'Math', 'Science']].sum(axis=1)
df.sort_values(by='Total', ascending = False, inplace = True)

print(df.head())