# create a dataframe for student msrks and print basic information like shape, columns, and data types
# data = {
#     'Name': ['Amit', 'Sagar', 'Pooja'],
#     'Math': [85, 90, 78],
#     'Science': [92, 88, 80],
#     'English': [75, 85, 82]
# }

import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("the number of rows and columns:", df.shape)
print("the columns are: ", df.columns)
print("the datatype of all the columns: ", df.dtypes)