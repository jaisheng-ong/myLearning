# webscraping.py - Your practice file

from bs4 import BeautifulSoup
import requests

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify()) #Display in a HTML format

# Extract the heading
heading = soup.find('h3').text
print(f"Heading: {heading}")

# Extract the paragraph
paragraph = soup.find('p').text
print(f"Paragraph: {paragraph}")

"""
# Get the Title
soup.title → Finds the <title> tag → Returns it with its content
"""
tag_object = soup.title
print("Tag Object:", tag_object)
print("tag object type:", type(tag_object))

"""
Get Player Name (h3 tags)

Note: If there are multiple tags with the same name, it returns the FIRST one!
HTML has:
<h3>Lebron James</h3>  ← Returns this one!
<h3>Stephen Curry</h3>
<h3>Kevin Durant</h3>
"""
# soup.title ← First <title> tag
# soup.p ← First <p> tag
# soup.b ← First <b> tag
tag_object = soup.h3
print("First <h3> Tag: ",tag_object)

print("=" * 50)
"""
Family Tree
        html (grandparent)
         |
       body (parent)
         |
    ┌────┴────┬────────┐
   h3        p        h3     (siblings - same level)
    |
    b                        (child - inside h3)

"""

tag_object = soup.h3  # Get the h3 tag
tag_child = tag_object.b  # Get the <b> tag inside h3
print("Tag Child: ", tag_child)

parent_tag = tag_child.parent  # Go UP to the parent
print("Child Tag's Parent: ", parent_tag)

print("Parent of <h3> tag: ", tag_object.parent)

print("-" *20)
sibing1 = tag_object.next_sibling
print("Sibling of <h3> tag:", sibing1) # Get the next element at the same level

sibling2 = sibing1.next_sibling
print("Sibling <p> tag: ", sibling2)

print(sibling2.next_sibling.next_sibling)


print("=" * 50)

"""
HTML Attributes
<tag attribute="value">Content</tag>

Examples:
<b id="boldest">Text</b>           ← id attribute
<a href="url.com">Link</a>         ← href attribute  
<img src="image.jpg">               ← src attribute
<div class="container">Content</div> ← class attribute


"""
print("Tag:", tag_child)
print("Tag ID:" ,tag_child.get('id'))  # Get the 'id' attribute safely
print("Tag Attributes: ", tag_child.attrs)  # Get ALL attributes as a dictionary

"""
            # Familiar with below
from bs4 import BeautifulSoup

html =
'<html>
<body>
    <a href="https://python.org" id="python-link" class="external">Python</a>
    <img src="logo.png" alt="Logo" width="100">
</body>
</html>'


soup = BeautifulSoup(html, 'html5lib')

# Get the link
link = soup.find('a')
print(link)
print("URL:", link['href'])           # https://python.org
print("ID:", link.get('id'))          # python-link
print("Class:", link['class'])        # ['external']
print("All attrs:", link.attrs)       # All attributes

# Get the image
img = soup.find('img')
print("Image source:", img['src'])    # logo.png
print("Alt text:", img.get('alt'))    # Logo
print("Width:", img['width'])         # 100
"""

print("=" * 50)

"""
    Navigable String

<b id="boldest">Lebron James</b>
      └────────┬────────┘
        This is the NavigableString!

Full Tag:  <b id="boldest">Lebron James</b>
           │                │
           └─ HTML markup   └─ TEXT (NavigableString)

"""
print("Full Tag:", tag_child)
print("Extract Text:", tag_child.string)
print("Type:", type(tag_child.string))

div = soup.find('body')
print(".string Returns None: (too many children or nested tags) ", div.string)  # None (multiple children!)
print(".get_text() is the solution:", div.get_text())  

"""
# Extract different text elements
heading = soup.find('h1').string
print("Heading:", heading)  # Welcome to Web Scraping

paragraph = soup.find('p').string
print("Paragraph:", paragraph)  # Learning BeautifulSoup is fun!

author = soup.find('b', id='author').string
print("Author:", author)  # John Doe

# Check type
print("Type:", type(author))  # <class 'bs4.element.NavigableString'>
"""

print("=" * 50)



"""
            Filter 1
            - find_all() method
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
"""

# Store HTML as string
table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"

# Parse it
table_bs = BeautifulSoup(table, 'html5lib')

table_rows = table_bs.find_all('tr')
print("Find all <tr> Tags in the table:")
print(table_rows)
firstRow = table_rows[0]
print("First Row:", firstRow)
print("Type:", type(firstRow)) #Tag object thus can use tag methods

print("First <td> tag in the row: ", firstRow.td)

# Rows
for i, row in enumerate(table_rows):
    print(f"Row {i} is {row}")

# Rows AND Columns
for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')  # Find all cells in this row
    for j, cell in enumerate(cells):
        print('column', j, "cell", cell)

"""
Row 0
  ├─ Column 0: <td id="flight">Flight No</td>
  ├─ Column 1: <td>Launch site</td>
  └─ Column 2: <td>Payload mass</td>
Row 1
  ├─ Column 0: <td>1</td>
  ├─ Column 1: <td><a href="...">Florida</a></td>
  └─ Column 2: <td>300 kg</td>
...
"""

print("Find all <tr> AND <td> tags:")
print(table_bs.find_all(name=["tr", "td"]))

print("-" * 50)
"""
        Filter 2
        - By Attributes
"""

print("Finding By ID: ", table_bs.find_all(id = "flight"))
# Finds all tags with id="flight"

print("Find by Links (href): ", table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida"))
print("Find any Tag with an Attribute:", table_bs.find_all('a', href=True))
# Finds all <a> tags that have ANY href attribute (regardless of value)

rows = table_bs.find_all('tr')
print(f"Total rows: {len(rows)}")  # 3

# Find all cells
cells = table_bs.find_all('td')
print(f"Total cells: {len(cells)}")  # 6

# Find all links
links = table_bs.find_all('a', href = True)
print(f"Total links: {len(links)}")  # 2

# Find header row by ID
header = table_bs.find_all(id='header')
print(f"Header: {header}")

print("Find element by Text:", table_bs.find_all(string = "Florida"))

"""
find_all() → Returns ALL matches (as a list)
find()     → Returns ONLY the FIRST match (as a single object)
"""
"""
New Tables (2 Tables)
📄 HTML Document
│
├─ 🚀 Table 1: Rocket Launch (class='rocket')
│   ├─ Row 1: Flight No | Launch site | Payload mass
│   ├─ Row 2: 1 | Florida | 300 kg
│   ├─ Row 3: 2 | Texas | 94 kg
│   └─ Row 4: 3 | Florida | 80 kg
│
└─ 🍕 Table 2: Pizza Party (class='pizza')
    ├─ Row 1: Pizza Place | Orders | Slices
    ├─ Row 2: Domino's Pizza | 10 | 100
    ├─ Row 3: Little Caesars | 12 | 144
    └─ Row 4: Papa John's | 15 | 165
"""
two_tables = "<h3>Rocket Launch </h3> \
<p><table class='rocket'> \
<tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> \
<tr><td>1</td><td>Florida</td><td>300 kg</td></tr> \
<tr><td>2</td><td>Texas</td><td>94 kg</td></tr> \
<tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p>\
<p><h3>Pizza Party</h3> \
<table class='pizza'> \
<tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> \
<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> \
<tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> \
<tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"

# Create BeautifulSoup object
two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

print("Return the first <table> tag:", two_tables_bs.find("table"))
print("Returns a desire class:", two_tables_bs.find("table", class_ = "pizza"))
