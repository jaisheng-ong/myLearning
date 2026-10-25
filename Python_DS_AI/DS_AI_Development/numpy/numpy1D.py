import numpy as np

# =============================================================================
# 1. CREATING ARRAYS
# =============================================================================

print("--- Creating Arrays ---")

a = np.array([0, 1, 2, 3, 4])           # Integer array
b = np.array([3.1, 11.02, 6.2])         # Float array
c = np.array(["Sam", "Lee", "Pei"])     # String array

print(f"Integer array: {a}")
print(f"Float array:   {b}")
print(f"String array:  {c}")


# =============================================================================
# 2. ARRAY ATTRIBUTES
# =============================================================================

print("\n--- Array Attributes ---")

print(f"type(a):  {type(a)}")     # <class 'numpy.ndarray'>
print(f"a.dtype:  {a.dtype}")     # int64 (data type of elements)
print(f"a.size:   {a.size}")      # 5 (number of elements)
print(f"a.ndim:   {a.ndim}")      # 1 (number of dimensions)
print(f"a.shape:  {a.shape}")     # (5,) (size in each dimension)
print(f"Version:  {np.__version__}")


# =============================================================================
# 3. ACCESSING ELEMENTS (Indexing)
# =============================================================================

print("\n--- Indexing ---")

arr = np.array([10, 20, 30, 40, 50])

print(f"arr[0]:   {arr[0]}")      # First element → 10
print(f"arr[-1]:  {arr[-1]}")     # Last element → 50
print(f"arr[2]:   {arr[2]}")      # Third element → 30


# =============================================================================
# 4. SLICING [start:end:step]
# =============================================================================

print("\n--- Slicing ---")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(f"arr[1:4]:   {arr[1:4]}")    # [2, 3, 4] (index 1 to 3)
print(f"arr[:4]:    {arr[:4]}")     # [1, 2, 3, 4] (start to 3)
print(f"arr[4:]:    {arr[4:]}")     # [5, 6, 7] (index 4 to end)
print(f"arr[1:5:2]: {arr[1:5:2]}")  # [2, 4] (step by 2)
print(f"arr[::2]:   {arr[::2]}")    # [1, 3, 5, 7] (every 2nd)


# =============================================================================
# 5. MODIFYING VALUES
# =============================================================================

print("\n--- Modifying Values ---")

arr = np.array([10, 20, 30, 40, 50])

# Single element
arr[0] = 100
print(f"After arr[0]=100:     {arr}")

# Multiple elements via slice
arr[3:5] = 300, 400
print(f"After arr[3:5]=300,400: {arr}")

# Using index list
index_list = [1, 2]
arr[index_list] = 999
print(f"After arr[[1,2]]=999: {arr}")


# =============================================================================
# 6. STATISTICAL FUNCTIONS
# =============================================================================

print("\n--- Statistical Functions ---")

arr = np.array([1, 2, 3, 4, 5])

print(f"sum():  {arr.sum()}")      # 15
print(f"mean(): {arr.mean()}")     # 3.0
print(f"std():  {arr.std()}")      # Standard deviation
print(f"min():  {arr.min()}")      # 1
print(f"max():  {arr.max()}")      # 5


# =============================================================================
# 7. ARRAY OPERATIONS (Element-wise)
# =============================================================================

print("\n--- Array Operations ---")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(f"a + b:  {np.add(a, b)}")        # [11, 22, 33]
print(f"a - b:  {np.subtract(a, b)}")   # [9, 18, 27]
print(f"a * b:  {np.multiply(a, b)}")   # [10, 40, 90]
print(f"a / b:  {np.divide(a, b)}")     # [10, 10, 10]

# Shorthand (same result)
# a + b, a - b, a * b, a / b


# =============================================================================
# 8. DOT PRODUCT
# =============================================================================

print("\n--- Dot Product ---")

x = np.array([1, 2])
y = np.array([3, 2])

# Dot product: 1*3 + 2*2 = 7
result = np.dot(x, y)
print(f"np.dot([1,2], [3,2]) = {result}")


# =============================================================================
# 9. SCALAR OPERATIONS (Broadcasting)
# =============================================================================

print("\n--- Scalar Operations ---")

arr = np.array([1, 2, 3, 4])

print(f"arr + 5:  {arr + 5}")      # [6, 7, 8, 9]
print(f"arr * 2:  {arr * 2}")      # [2, 4, 6, 8]
print(f"arr - 1:  {arr - 1}")      # [0, 1, 2, 3]


# =============================================================================
# 10. MATHEMATICAL FUNCTIONS
# =============================================================================

print("\n--- Math Functions ---")

print(f"np.pi: {np.pi}")

x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(f"sin([0, π/2, π]): {np.round(y, 2)}")  # [0, 1, 0]

# Other functions: np.cos(), np.exp(), np.log(), np.sqrt()


# =============================================================================
# 11. LINSPACE (Evenly spaced values)
# =============================================================================

print("\n--- Linspace ---")

# np.linspace(start, stop, num)
arr = np.linspace(0, 10, num=5)
print(f"linspace(0, 10, 5): {arr}")  # [0, 2.5, 5, 7.5, 10]

# Useful for plotting
# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)


# =============================================================================
# 12. RESHAPE
# =============================================================================

print("\n--- Reshape ---")

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)  # 2 rows, 3 columns
print(f"Original: {arr}")
print(f"Reshaped (2,3):\n{reshaped}")

column = arr.reshape(6, 1)    # Column vector
print(f"Column vector:\n{column.T}")  # Transpose for display


# =============================================================================
# 13. FILTERING (Boolean indexing)
# =============================================================================

print("\n--- Filtering ---")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(f"arr > 5:       {arr[arr > 5]}")      # [6, 7, 8]
print(f"Even numbers:  {arr[arr % 2 == 0]}") # [2, 4, 6, 8]
print(f"Odd numbers:   {arr[arr % 2 == 1]}") # [1, 3, 5, 7]


# =============================================================================
# 14. ITERATING
# =============================================================================

print("\n--- Iterating ---")

arr = np.array([10, 20, 30])

print("Loop through array:")
for x in arr:
    print(f"  {x}")
