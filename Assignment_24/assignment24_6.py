from assignment24_1 import df

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

df['Status'] = df['Total'].apply(lambda x: 'pass' if x >= 250 else 'fail')

counter = 0
for status in df['Status']:
    if status == 'pass':
        counter = counter + 1
print("the number of passed students: ",counter)

