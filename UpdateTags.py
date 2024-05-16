import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('Library.xml')
root = tree.getroot()

# Replace <date> tags with <string>
for elem in root.iter():
    if elem.tag == 'date':
        elem.tag = 'string'

# Write modified XML content to a new file
tree.write('Library_cleaned.xml')
