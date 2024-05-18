import xml.etree.ElementTree as ET
import plistlib
import json

# Parse the XML file
tree = ET.parse('Library.xml')
root = tree.getroot()

# Replace <date> tags with <string>
for elem in root.iter():
    if elem.tag == 'date':
        elem.tag = 'string'

# Write modified XML content to a new file
tree.write('Library_cleaned.xml')

with open('Library_cleaned.xml', 'rb') as f:
    plist_data = plistlib.load(f)

# Convert to JSON
json_data = json.dumps(plist_data)

# Write to JSON file
with open('Library_cleaned.json', 'w') as f:
    f.write(json_data)


def add_missing_keys_in_tracks(tracks_data, expected_key):
    for track_id, track_info in tracks_data.items():
        for key in expected_key:
            if key not in track_info:
                track_info[key] = 0

def check_and_update_json(json_file_path, expected_key):
    # Load JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Check if "Tracks" key exists
    if "Tracks" in data:
        tracks_data = data["Tracks"]
        # Add missing keys in each track
        add_missing_keys_in_tracks(tracks_data, expected_key)
    else:
        print("No 'Tracks' key found in the JSON file.")

    # Write the updated JSON back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

json_file_path = "Library_cleaned.json"
expected_key = ["Play Count"]
check_and_update_json(json_file_path, expected_key)
