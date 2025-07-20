import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

x = df[['Age', 'Salary']]      
y = df['Purchased']            

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)