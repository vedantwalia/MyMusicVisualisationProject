import json

def add_missing_keys_in_tracks(tracks_data, expected_keys):
    for track_id, track_info in tracks_data.items():
        for key in expected_keys:
            if key not in track_info:
                track_info[key] = 0

def check_and_update_json(json_file_path, expected_keys):
    # Load JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Check if "Tracks" key exists
    if "Tracks" in data:
        tracks_data = data["Tracks"]
        # Add missing keys in each track
        add_missing_keys_in_tracks(tracks_data, expected_keys)
    else:
        print("No 'Tracks' key found in the JSON file.")

    # Write the updated JSON back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Example usage:
json_file_path = "Library_cleaned.json"  # Replace with the path to your JSON file
expected_keys = ["Play Count"]  # Add more keys as needed
check_and_update_json(json_file_path, expected_keys)
