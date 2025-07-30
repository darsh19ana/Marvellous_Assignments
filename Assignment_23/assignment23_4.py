# display students who scored more than 85 in science

from assignment23_1 import df

high_scorers = df[df['Science'] > 85][['Name', 'Science']]
print("students who scored more than 85 in science:")
print(high_scorers)