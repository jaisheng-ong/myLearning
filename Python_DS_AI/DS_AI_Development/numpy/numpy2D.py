import numpy as np

# =============================================================================
# 1. ARRAY CREATION
# =============================================================================

print("--- Array Creation ---")

# From nested list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
print(f"From list:\n{A}")

# Using np.ones() and np.zeros()
matrix = np.ones((3, 2)) #default element type = float
matrix_int = np.ones((3, 2), dtype=int)
zeros = np.zeros((2, 3))

print(f"\nnp.ones((3,2)):\n{matrix}")
print(f"dtype: {matrix.dtype}")

print(f"\nnp.ones with int:\n{matrix_int}")
print(f"dtype: {matrix_int.dtype}")

print(f"\nnp.zeros((2,3)):\n{zeros}")

# Identity matrix (a square matrix with 1s on the diagonal and 0s elsewhere)
eye = np.eye(3, 4)
print(f"\nnp.eye(3, 4):\n{eye}")


# =============================================================================
# 2. ARRAY ATTRIBUTES
# =============================================================================

print("\n--- Array Attributes ---")

A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

print(f"Array:\n{A}")
print(f"ndim:  {A.ndim}")    # 2 (dimensions)
print(f"shape: {A.shape}")   # (3, 3) (rows, cols)
print(f"size:  {A.size}")    # 9 (total elements)
print(f"dtype: {A.dtype}")   # int64


# =============================================================================
# 3. ACCESSING ELEMENTS (Indexing)
# =============================================================================

print("\n--- Indexing ---")

A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

# Single element: A[row, col]
print(f"A[1, 2]: {A[1, 2]}")    # Row 1, Col 2 → 23
print(f"A[0, 0]: {A[0, 0]}")    # Row 0, Col 0 → 11
print(f"A[2][1]: {A[2][1]}")    # Alternative syntax → 32


# =============================================================================
# 4. SLICING 2D ARRAYS
# =============================================================================

print("\n--- Slicing ---")

A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

# First row, first 2 columns
print(f"A[0, 0:2]:  {A[0, 0:2]}")      # [11, 12]

# First 2 rows, 3rd column
print(f"A[0:2, 2]:  {A[0:2, 2]}")      # [13, 23]

# All rows, first column
print(f"A[:, 0]:    {A[:, 0]}")        # [11, 21, 31]

# All columns, first row
print(f"A[0, :]:    {A[0, :]}")        # [11, 12, 13]

# Submatrix (first 2 rows, first 2 cols)
print(f"A[0:2, 0:2]:\n{A[0:2, 0:2]}")


# =============================================================================
# 5. ELEMENT-WISE ARITHMETIC
# =============================================================================

print("\n--- Element-wise Arithmetic ---")

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print(f"X:\n{X}")
print(f"Y:\n{Y}")

print(f"\nX + Y:\n{X + Y}")    # Addition
print(f"X - Y:\n{X - Y}")      # Subtraction
print(f"X * Y:\n{X * Y}")      # Element-wise multiplication (Hadamard product)
print(f"X / Y:\n{X / Y}")      # Division


# =============================================================================
# 6. SCALAR ARITHMETIC (Broadcasting)
# =============================================================================

print("\n--- Scalar Arithmetic ---")

Y = np.array([[2, 1], [1, 2]])
print(f"Y:\n{Y}")

print(f"\nY * 2:\n{Y * 2}")    # Multiply all by 2
print(f"Y + 10:\n{Y + 10}")   # Add 10 to all
print(f"Y - 1:\n{Y - 1}")     # Subtract 1 from all
print(f"Y / 2:\n{Y / 2}")     # Divide all by 2


# =============================================================================
# 7. ELEMENT-WISE FUNCTIONS
# =============================================================================

print("\n--- Element-wise Functions ---")

A = np.array([[0, 1], [2, 3]])

print(f"A:\n{A}")
print(f"\nnp.sin(A):\n{np.round(np.sin(A), 2)}")
print(f"np.exp(A):\n{np.round(np.exp(A), 2)}")
print(f"np.sqrt(A):\n{np.round(np.sqrt(A), 2)}")
print(f"np.log(A+1):\n{np.round(np.log(A+1), 2)}")  # +1 to avoid log(0)


# =============================================================================
# 8. SUM AND MEAN
# =============================================================================

print("\n--- Sum and Mean ---")

A = np.array([[1, 2, 3], [4, 5, 6]])
print(f"A:\n{A}")

print(f"\nTotal sum:     {A.sum()}")         # 21
print(f"Mean:          {A.mean()}")          # 3.5
print(f"Sum by column: {A.sum(axis=0)}")     # [5, 7, 9]
print(f"Sum by row:    {A.sum(axis=1)}")     # [6, 15]
print(f"Mean by column:{A.mean(axis=0)}")    # [2.5, 3.5, 4.5]
print(f"Mean by row:   {A.mean(axis=1)}")    # [2, 5]


# =============================================================================
# 9. MAX AND MIN VALUES
# =============================================================================

print("\n--- Max and Min ---")

A = np.array([[1, 2, 3], [4, 5, 6]])
print(f"A:\n{A}")

print(f"\nMax:           {A.max()}")          # 6
print(f"Min:           {A.min()}")            # 1
print(f"Max by column: {A.max(axis=0)}")      # [4, 5, 6]
print(f"Min by row:    {A.min(axis=1)}")      # [1, 4]
print(f"Argmax:        {A.argmax()}")         # 5 (flattened index)
print(f"Argmin:        {A.argmin()}")         # 0 (flattened index)


# =============================================================================
# 10. RESHAPING
# =============================================================================

print("\n--- Reshaping ---")

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Original: {arr}")

# Reshape to 2D
reshaped = arr.reshape(2, 3)
print(f"\nreshape(2, 3):\n{reshaped}")

reshaped2 = arr.reshape(3, 2)
print(f"\nreshape(3, 2):\n{reshaped2}")

# Flatten back to 1D
flat = reshaped.flatten()
print(f"\nflatten(): {flat}")


# =============================================================================
# 11. TRANSPOSITION
# =============================================================================

print("\n--- Transposition ---")

C = np.array([[1, 1], [2, 2], [3, 3]])
print(f"Original C (3x2):\n{C}")

print(f"\nC.T (2x3):\n{C.T}")  # Rows become columns, columns become rows


# =============================================================================
# 12. MATRIX MULTIPLICATION (Dot Product)
# =============================================================================

print("\n--- Matrix Multiplication ---")

# A (2x3) @ B (3x2) = Result (2x2)
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])

print(f"A (2x3):\n{A}")
print(f"\nB (3x2):\n{B}")

# Using np.dot()
Z = np.dot(A, B)
print(f"\nnp.dot(A, B):\n{Z}")

# Using @ operator (same result)
Z2 = A @ B
print(f"\nA @ B:\n{Z2}")

# Note: X * Y is element-wise, np.dot(X, Y) is matrix multiplication


# =============================================================================
# QUICK REFERENCE
# =============================================================================

"""
INDEXING & SLICING:
  A[row, col]       - Single element
  A[r1:r2, c1:c2]   - Submatrix
  A[:, 0]           - All rows, first column
  A[0, :]           - First row, all columns

OPERATIONS:
  X + Y, X - Y      - Element-wise add/subtract
  X * Y             - Element-wise multiply (Hadamard)
  np.dot(X, Y)      - Matrix multiplication
  X @ Y             - Matrix multiplication (Python 3.5+)

AGGREGATION:
  A.sum()           - Total sum
  A.sum(axis=0)     - Sum columns (collapse rows)
  A.sum(axis=1)     - Sum rows (collapse columns)

RESHAPING:
  A.reshape(r, c)   - Change shape
  A.T               - Transpose
  A.flatten()       - Convert to 1D
"""
