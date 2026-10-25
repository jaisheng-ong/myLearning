"""
XML File
"""
"""
# Create the root element
employee = etree.Element('employee')

# Add child elements
details = etree.SubElement(employee, 'details')
first = etree.SubElement(details, 'firstname')
second = etree.SubElement(details, 'lastname')
third = etree.SubElement(details, 'age')

# Set the text content
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# Create tree and write to file
mydata1 = etree.ElementTree(employee)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

"""

import xml.etree.ElementTree as etree
import pandas as pd

tree = etree.parse("gdp.xml")
root = tree.getroot()

# Automatically discover columns from the first node
if len(root) > 0:
    # Get all child tag names from the first node
    first_node = root[0]

    columns = []
    for child in first_node:
        if child.tag:  # the tags
            columns.append(child.tag)
            
    print(f"Discovered columns: {columns}")
    
    # Collect data from all nodes
    data = []
    for node in root: # Outer Loop

        row = []
        for child in node: # Inner Loop
            if child.text:  # the value
                row.append(child.text)
        data.append(row)
    
    # Create DataFrame
    df_xml = pd.DataFrame(data, columns=columns)
    print(df_xml)
else:
    print("No data found in XML file")


# Read XML directly into DataFrame
# df = pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details")
