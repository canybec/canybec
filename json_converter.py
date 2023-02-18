import json

# Open the JSON file and load its contents
with open('aisimp_embeddings8.json') as f:
    data = json.load(f)

# Define a function to recursively search for numeric values and convert them to strings
def convert_to_string(obj):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = convert_to_string(obj[i])
        return obj
    elif isinstance(obj, dict):
        for key in obj:
            obj[key] = convert_to_string(obj[key])
            if key == "id" and isinstance(obj[key], int):
                obj[key] = str(obj[key])
        return obj
    elif isinstance(obj, int):
        return str(obj)
    else:
        return obj

# Convert any numeric values after "id" to strings
data = convert_to_string(data)

# Save the modified data back to the JSON file
with open('aisimp_embeddings22.json', 'w') as f:
    json.dump(data, f)
