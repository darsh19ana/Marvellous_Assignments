from assignment24_1 import df

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

df['Status'] = df['Total'].apply(lambda x: 'pass' if x >= 250 else 'fail')

print(df)