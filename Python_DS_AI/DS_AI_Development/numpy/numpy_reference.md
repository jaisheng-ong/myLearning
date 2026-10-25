# NumPy Reference

## Array (ndarray)

A **NumPy array** is a fast, fixed-type multidimensional container.

### Attributes

| Attribute | Description |
|-----------|-------------|
| `arr.shape` | Dimensions (rows, columns) |
| `arr.ndim` | Number of dimensions |
| `arr.size` | Total number of elements |
| `arr.dtype` | Data type of elements |
| `arr.T` | Transpose |

### Array Creation

| Function | Description |
|----------|-------------|
| `np.array([1,2,3])` | Create from list |
| `np.zeros((r,c))` / `np.ones((r,c))` | Array of zeros / ones |
| `np.empty((r,c))` | Uninitialized array |
| `np.arange(start,stop,step)` | Range of values |
| `np.linspace(start,stop,n)` | n evenly spaced values |
| `np.eye(n)` / `np.identity(n)` | Identity matrix |
| `np.random.rand(r,c)` | Random values (0 to 1) |
| `np.random.randint(low,high,size)` | Random integers |

### Reshaping

| Method | Description |
|--------|-------------|
| `arr.reshape(r,c)` | Change shape |
| `arr.flatten()` / `arr.ravel()` | Flatten to 1D |
| `arr.resize(r,c)` | Resize in place |
| `np.concatenate([a,b])` | Join arrays |
| `np.vstack([a,b])` / `np.hstack([a,b])` | Stack vertically / horizontally |
| `np.split(arr,n)` | Split into n parts |

### Math Operations

| Function | Description |
|----------|-------------|
| `arr.sum()` / `arr.mean()` / `arr.min()` / `arr.max()` | Aggregate functions |
| `arr.std()` / `arr.var()` | Standard deviation / Variance |
| `np.sqrt(arr)` / `np.exp(arr)` / `np.log(arr)` | Element-wise math |
| `np.abs(arr)` | Absolute values |
| `np.round(arr,decimals)` | Round values |
| `np.dot(a,b)` / `a @ b` | Matrix multiplication |
| `arr.cumsum()` / `arr.cumprod()` | Cumulative sum / product |

### Indexing & Slicing

| Syntax | Description |
|--------|-------------|
| `arr[0]` | First element |
| `arr[-1]` | Last element |
| `arr[1:4]` | Slice (index 1 to 3) |
| `arr[::2]` | Every 2nd element |
| `arr[arr > 5]` | Boolean filtering |
| `arr[row, col]` | 2D indexing |
| `arr[:, 0]` | All rows, first column |

### Sorting & Searching

| Function | Description |
|----------|-------------|
| `np.sort(arr)` / `arr.sort()` | Sort array |
| `np.argsort(arr)` | Indices that would sort |
| `np.where(condition)` | Indices where condition is True |
| `np.argmax(arr)` / `np.argmin(arr)` | Index of max / min |

---

## Quick Examples

```python
import numpy as np
import matplotlib.pyplot as plt ## For ploting functions

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))

# Basic operations
arr * 2          # [2, 4, 6, 8, 10]
arr + arr        # element-wise addition

# Stats
arr.mean()       # 3.0
arr.sum()        # 15

# Reshape
arr.reshape(5, 1)  # column vector

# Filter
arr[arr > 2]     # [3, 4, 5]
```