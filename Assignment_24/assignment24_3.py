import pandas as pd

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
    'Gender': ['Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

grouped_df = df.groupby('Gender')
subjects = ['Math', 'Science', 'English']

avg_marks = grouped_df[subjects].mean()

print(avg_marks)