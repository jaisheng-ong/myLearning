"""
        In Short

1. LOAD DATA
   ├─ pd.read_csv()
   └─ Create DataFrame
   
2. EXPLORE DATA
   ├─ df.head() / df.tail()
   ├─ df.shape
   └─ Quick visual inspection
   
3. STATISTICAL OVERVIEW
   ├─ df.info() → Structure & types
   └─ df.describe() → Statistics
   
4. CHECK DATA QUALITY
   ├─ df.isnull() → Find missing values
   ├─ .value_counts() → Count missing
   └─ df.dtypes → Verify data types
   
5. VISUALIZE
   ├─ plt.pie() / plt.bar() / plt.hist()
   └─ Get insights from patterns

"""



import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

df = pd.read_csv(path)

print(df.head(5)) # Get the first 5 rows
print(df.tail(5))  # Last 5 rows

print(df.shape) # Output (768, 9) -- 768 rows and 9 columns

print(df.info())
"""
.info() tells you:
✅ Total entries (768)
✅ Column names
✅ Non-null counts (checks for missing data)
✅ Data types (int64, float64)
✅ Memory usage
"""

print(df.describe())
"""
.describe() shows:
count = Number of values
mean = Average
std = Standard deviation (spread)
min = Minimum value
25% = First quartile (25th percentile)
50% = Median (middle value)
75% = Third quartile (75th percentile)
max = Maximum value
"""

"""
        Check for Missing Data

- False = Value is present (NOT missing)
- True = Value is missing
""" 
missing_data = df.isnull()
print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
"""
Loop through each column name
       ↓
For "Pregnancies" column:
    Count how many True (missing) and False (present)
       ↓
Output:
    Pregnancies
    False    768  ← All 768 values are present
    
       ↓
Repeat for all columns...
"""
print(df.dtypes)

"""
Numerical variables should be int64 or float64 ✅
If text was stored as numbers, need to convert
If numbers stored as strings, calculations won't work
"""

# Change data types if needed
# df['column_name'] = df['column_name'].astype(float)

import matplotlib.pyplot as plt

"""
    Visualize using Pie Chart
"""
labels = 'Not Diabetic', 'Diabetic'
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()