import json

# Function to append data to the JSON file with the date as the key
def append_to_json_file(data, file_name):
    try:
        with open('data.json', 'r') as file:
            all_data = json.load(file)
    except FileNotFoundError:
        all_data = {}

    all_data[file_name] = data

    with open('data.json', 'w') as file:
        json.dump(all_data, file, indent=4)
