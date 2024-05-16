import plistlib
import json

# Load plist file
with open('Library_cleaned.xml', 'rb') as f:
    plist_data = plistlib.load(f)

# Convert to JSON
json_data = json.dumps(plist_data)

# Write to JSON file
with open('Library_cleaned.json', 'w') as f:
    f.write(json_data)