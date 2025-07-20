# plot a line chart of marks 'Amit' across all subjects.a

from assignment23_1 import df
import numpy as np
import matplotlib.pyplot as plt

df['Total'] = df[['English', 'Math', 'Science']].sum(axis=1)

amit = df[df['Name'] == 'Amit']

subjects = ['English', 'Math', 'Science']
amit_marks = amit[subjects].values.flatten()

plt.plot(subjects, amit_marks, marker='o')
plt.title("Amit's Marks Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()