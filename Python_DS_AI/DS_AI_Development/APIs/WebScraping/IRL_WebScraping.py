from bs4 import BeautifulSoup
import requests

import pandas as pd

url = "http://www.ibm.com"

data = requests.get(url).text

"""
requests.get(url) → Downloads the webpage
.text → Converts the response to text (HTML as a string)
data → Now contains the entire HTML source code

Internet
   │
   ├─ http://www.ibm.com
   │       │
   │       └─ requests.get()
   │              │
   │              ▼
   └────► HTML source code (as text)
              │
              └─ Stored in variable: data
"""

soup = BeautifulSoup(data, "html5lib")
"""
BEFORE:
data = "<html><body><a href='...'>Link</a></body></html>"
       └─ Just a long string of text ❌

AFTER:
soup = BeautifulSoup(data, "html5lib")
       └─ Structured, searchable object ✅
       
Now we can do:
soup.find('a')
soup.find_all('img')
etc.
"""

# Scrape All Links
for link in soup.find_all('a', href = True):
    print(link.get('href'))

print("-" * 50)

# Scrape ALl Images
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

print("-" * 50)

target_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(target_url).text

soup = BeautifulSoup(data, "html5lib")

# Find the first table
table = soup.find('table')

# Loop through each row
for row in table.find_all('tr'):
    # Get all columns (cells) in each row
    #print(row)
    cols = row.find_all('td')
    
    # Extract specific columns
    color_name = cols[2].string  # Column 3 (index 2)
    color_code = cols[3].text    # Column 4 (index 3)
    
    # Print the result
    print(f"{color_name}--->{color_code}")

print("=" *50)
"""
    Scraping Tables with Pandas

-Pandas automatically finds all <table> tags on the page
-Parses each table into a DataFrame
-Returns a list of DataFrames
"""
pd_table = pd.read_html(target_url)
print("This is a LIST of DataFrames:")
print(type(pd_table))  # <class 'list'>
print(f"Number of tables: {len(pd_table)}")

print("\n" + "="*50 + "\n")

# Get the first (and only) DataFrame
df = pd_table[0]

print("This is a SINGLE DataFrame:")
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(f"Shape: {df.shape}")
print("\nData:")
print(df)

df = pd_table[0]

# Get a specific column
colorNames = df[2]
print(colorNames)

# Select only the columns we need
clean_df = df[[2, 3]]

# Rename columns
clean_df.columns = ['Color Name', 'Color Code']

# Slice Away the original header - remove header row 
clean_df = clean_df[1:]

print(clean_df)



