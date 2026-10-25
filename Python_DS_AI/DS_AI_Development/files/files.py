# =============================================================================
# 1. FILE MODES
# =============================================================================

"""
Mode  | Description
------|--------------------------------------------------
'r'   | Read only (default) - file must exist
'w'   | Write only - creates new or overwrites existing
'a'   | Append - adds to end of file
'r+'  | Read and write - file must exist
'w+'  | Write and read - creates new or overwrites
'a+'  | Append and read - creates if doesn't exist
"""


# =============================================================================
# 2. WRITING FILES
# =============================================================================

print("--- Writing Files ---")

# Create and write to a file
with open("demo.txt", "w") as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python is fun\n")
    f.write("Line 3: File handling")

print("File 'demo.txt' created.")


# =============================================================================
# 3. READING FILES
# =============================================================================

print("\n--- Reading Files ---")

# Method 1: read() - reads entire file as string
with open("demo.txt", "r") as f:
    content = f.read()
    print("read():")
    print(content)

# Method 2: readline() - reads one line at a time
print("\nreadline():")
with open("demo.txt", "r") as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Method 3: readlines() - returns list of all lines
print("\nreadlines():")
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(f"Lines as list: {lines}")


# =============================================================================
# 4. LOOPING THROUGH FILES
# =============================================================================

print("\n--- Looping Through Files ---")

with open("demo.txt", "r") as f:
    line_count = 0
    for line in f:
        print(f"  {line.strip()}")
        line_count += 1
    print(f"Total lines: {line_count}")


# =============================================================================
# 5. CONDITIONAL READING (Break on keyword)
# =============================================================================

print("\n--- Conditional Reading ---")

# Create test file
with open("search.txt", "w") as f:
    f.write("Normal line\n")
    f.write("This contains ERROR here\n")
    f.write("This won't be read\n")

# Read until keyword found
with open("search.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:  # End of file
            break
        if "ERROR" in line:
            print(f"Found ERROR: {line.strip()}")
            break
        print(f"Read: {line.strip()}")


# =============================================================================
# 6. CURSOR POSITION - seek() and tell()
# =============================================================================

print("\n--- Cursor Position ---")

with open("demo.txt", "r") as f:
    print(f"Initial position: {f.tell()}")      # 0
    
    f.readline()                                 # Read first line
    print(f"After readline(): {f.tell()}")      # Position after line 1
    
    f.seek(0)                                    # Reset to beginning
    print(f"After seek(0): {f.tell()}")         # 0
    
    f.seek(10)                                   # Jump to byte 10
    print(f"Read from byte 10: {f.read(5)}")    # Read 5 chars


# =============================================================================
# 7. APPEND MODE
# =============================================================================

print("\n--- Append Mode ---")

# 'a' mode adds to end without overwriting
with open("demo.txt", "a") as f:
    f.write("\nLine 4: Appended line")

# 'a+' allows both append and read
with open("demo.txt", "a+") as f:
    f.write("\nLine 5: Another append")
    f.seek(0)  # Must seek to read
    print("After appending:")
    print(f.read())


# =============================================================================
# 8. COPY FILE CONTENTS
# =============================================================================

print("\n--- Copy File Contents ---")

with open("demo.txt", "r") as source:
    with open("copy.txt", "w") as dest:
        for line in source:
            dest.write(line)

print("Copied demo.txt → copy.txt")


# =============================================================================
# 9. TRUNCATE - Cut off file content
# =============================================================================

print("\n--- Truncate ---")

# Create test file
with open("truncate_test.txt", "w") as f:
    f.write("Keep this line\nDelete this line")

# truncate() - cuts from current cursor position
with open("truncate_test.txt", "r+") as f:
    f.readline()      # Move cursor past first line
    f.truncate()      # Delete everything after cursor
    
    f.seek(0)
    print(f"After truncate(): '{f.read()}'")

# truncate(0) - empties entire file
with open("truncate_test.txt", "r+") as f:
    f.truncate(0)
    print("After truncate(0): file is empty")


# =============================================================================
# 10. ERROR HANDLING
# =============================================================================

print("\n--- Error Handling ---")

file_name = "nonexistent.txt"

try:
    with open(file_name, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: '{file_name}' not found")
except Exception as e:
    print(f"Error: {e}")


# =============================================================================
# QUICK REFERENCE
# =============================================================================

"""
COMMON PATTERNS:

# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Write to file (overwrites)
with open("file.txt", "w") as f:
    f.write("content")

# Append to file
with open("file.txt", "a") as f:
    f.write("new content")

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read into list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Copy file
with open("src.txt", "r") as src:
    with open("dst.txt", "w") as dst:
        dst.write(src.read())
"""

