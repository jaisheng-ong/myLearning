# Pandas Reference

## Series

A **Series** is a 1D labeled array (like a column).

### Attributes

| Attribute | Description |
|-----------|-------------|
| `s.values` | Returns data as NumPy array |
| `s.index` | Returns index labels |
| `s.dtype` | Data type of values |
| `s.shape` | Tuple of dimensions |
| `s.size` | Number of elements |
| `s.name` | Name of the Series |

### Methods

| Method | Description |
|--------|-------------|
| `s.head(n)` | First n rows (default 5) |
| `s.tail(n)` | Last n rows |
| `s.unique()` / `s.nunique()` | Unique values / Count of unique values |
| `s.value_counts()` | Count of each unique value |
| `s.sum()` | Sum of values |
| `s.mean()` | Average |
| `s.min()` / `s.max()` | Min / Max value |
| `s.sort_values()` / `s.sort_index()` | Sort by values / Sort by index |
| `s.isnull()` / `s.notnull()` | Check for missing / non-missing values |
| `s.fillna(value)` | Replace missing values |
| `s.apply(func)` | Apply function to each element |

---

## DataFrame

A **DataFrame** is a 2D table (rows and columns).

### Attributes

| Attribute | Description |
|-----------|-------------|
| `df.values` | Data as 2D NumPy array |
| `df.index` | Row labels |
| `df.columns` | Column labels |
| `df.dtypes` | Data type of each column |
| `df.shape` | (rows, columns) |
| `df.size` | Total number of elements |
| `df.T` | Transpose (swap rows/columns) |

### Methods

| Method | Description |
|--------|-------------|
| `df.head(n)` | First n rows |
| `df.tail(n)` | Last n rows |
| `df.info()` | Summary of DataFrame |
| `df.describe()` | Statistics for numeric columns |
| `df.sum()` / `df.mean()` / `df.min()` / `df.max()` | Aggregate functions for columns |
| `df.sort_values(by)` | Sort by column |
| `df.drop(col, axis=1)` | Remove column |
| `df.rename(columns={})` | Rename columns |
| `df.isnull()` | Check for missing values |
| `df.fillna(value)` | Fill missing values |
| `df.dropna()` | Remove rows with missing values |
| `df.groupby(col)` | Group by column |
| `df.merge(df2)` | Join two DataFrames |
| `df.apply(func)` | Apply function to columns/rows |
| `df.to_csv('file.csv')` | Export to CSV |

---

## Quick Examples

```python
import pandas as pd

# Create Series
s = pd.Series([1, 2, 3], name='numbers')

# Create DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Read CSV
df = pd.read_csv('file.csv')

# Select column
df['column_name']  # returns Series

# Filter rows
df[df['column'] > 5]

# Add new column
df['new_col'] = df['A'] + df['B']
```

