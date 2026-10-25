
"""
CSV File
"""
import pandas as pd
import numpy as np

file = "output.csv"

df = pd.read_csv(file)
df.columns = ["Name", "ID", "Level", "Description"]
#print(df)

"""
    Selecting Columns
"""
print(df["Name"]) # single column
print("-" * 5)
print(df[["Name", "Level", "Description"]]) # multiple columns

"""
    Selecting rows (.iloc & .loc)
"""

print(df.iloc[0]) # First Row
print("=" * 5)
print(df.loc[[0,1,2], "Name"]) # Multiple Rows

print("=" * 5)
print(df.iloc[[0,1,2], 0]) # Same as above but different fuction


# creating a dataframe
df1=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
#print(df1)

#applying the transform function
df1 = df1.transform(func = lambda x : x + 10)
print(df1)

# Square root value of each value in the table
result = df1.transform(func = ['sqrt'])
print(result)
