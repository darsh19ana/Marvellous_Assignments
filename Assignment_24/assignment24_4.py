from assignment24_1 import df
import matplotlib.pyplot as plt

marks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].values.flatten()
subjects = ['Math', 'Science', 'English']

plt.pie(marks, labels=subjects)
plt.show()

