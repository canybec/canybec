import json
import os

# Maximum size of each output JSON file in bytes
MAX_SIZE = 2000000

# Open the JSON file and load its contents
with open('data.json', 'r') as f:
    data = json.load(f)

# Get the list of vectors from the data
vectors = data["vectors"]

# Divide the vectors into smaller chunks
chunks = []
current_chunk = []
current_size = 0
for vector in vectors:
    vector_size = json.dumps(vector).encode('utf-8').__sizeof__()
    if current_size + vector_size > MAX_SIZE:
        chunks.append(current_chunk)
        current_chunk = []
        current_size = 0
    current_chunk.append(vector)
    current_size += vector_size
chunks.append(current_chunk)

# Create a new dictionary to hold the chunks of vectors
output_data = {"vectors": []}

# Write each chunk to a separate JSON file
for i, chunk in enumerate(chunks):
    output_data["vectors"] = chunk
    filename = f'output_{i}.json'
    with open(filename, 'w') as f:
        json.dump(output_data, f)
    size = os.path.getsize(filename)
    print(f'Saved {filename} ({size} bytes)')
    assert size <= MAX_SIZE, f"Error: chunk {i} is larger than {MAX_SIZE} bytes"
assert sum(os.path.getsize(f'output_{i}.json') for i in range(len(chunks))) == os.path.getsize('large_data.json'), "Error: chunks do not add up to the total size of the data"
