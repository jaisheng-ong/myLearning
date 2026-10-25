import pandas as pd 

# =============================================================================
# 1. LOADING DATA FROM CSV
# =============================================================================

df = pd.read_csv('c:/Users/ongja/Downloads/Coursera/pandas/students.csv') # API Call

print("--- CSV Data ---")
print(df.head())              # First 5 rows
print(f"Shape: {df.shape}")   # (rows, columns)


# =============================================================================
# 2. SERIES - 1D labeled array
# =============================================================================

print("\n--- Series ---")

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Accessing elements
print(f"By label s[2]:    {s[2]}")      # Label 2 → 30
print(f"By position iloc: {s.iloc[3]}") # Position 3 → 40
print(f"Slice s[1:4]:\n{s[1:4]}")       # Range


# =============================================================================
# 3. DATAFRAME - 2D table
# =============================================================================

print("\n--- DataFrame ---")

x = {
    'Name': ['Lai Khor Yuan', 'Loh Sook Yee', 'Sek Jing Tong', 'Ting Zhen', 'Ku Wanqing'], 
    'ID': ['520', '890', '312', '575', '973'],
    'Level': [10, 10, 6, 4, 8]
}

df = pd.DataFrame(x, index=['a', 'b', 'c', 'd', 'e'])
print(df)


# =============================================================================
# 4. SELECTING DATA
# =============================================================================

print("\n--- Selecting Data ---")

# Select column
print("Column 'Name':")
print(df['Name'])

# Select row by label (loc) vs position (iloc)
print(f"\nRow 'd' (loc):  {df.loc['d'].tolist()}")
print(f"Row 2 (iloc):   {df.iloc[2].tolist()}")

# Select multiple columns
print("\nMultiple columns ['Name', 'ID']:")
print(df[['Name', 'ID']])

# Select rows by slicing
print("\nRows 1:3 (slice):")
print(df[1:3])


# =============================================================================
# 5. FILTERING & UNIQUE VALUES
# =============================================================================

print("\n--- Filtering ---")

unique_ids = df['ID'].unique()
print(f"Unique IDs: {unique_ids}")

# Filter rows where Level > 5
high_level = df[df['Level'] > 5]
print("\nLevel > 5:")
print(high_level)


# =============================================================================
# 6. ADDING COLUMNS & SAVING
# =============================================================================

print("\n--- Add Column & Save ---")

df['Combined'] = df['Name'] + ' (Lvl ' + df['Level'].astype(str) + ')'
print(df)

# Save to CSV
df.to_csv('output.csv', index=False)
print("\nSaved to output.csv")
