import json

# Replace with your .jsonl file path
file_path = 'courses_202509.jsonl'

with open(file_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

# Now `data` is a list of dictionaries (or whatever your JSON lines represent)

