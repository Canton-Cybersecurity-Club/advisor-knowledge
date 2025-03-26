import os
import json

def combine_json_files(directory_path, output_file):
    combined_data = []
    data_map = {}

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):  # Check if the file is a JSON file
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    combined_data.append(data)
                    data_map[filename] = {'record_count': len(data)}  # You can customize what info to store
                except json.JSONDecodeError as e:
                    print(f"Error decoding {filename}: {e}")

    # Create the combined structure with a map of the contents
    result = {
        'knowledge_data_map': data_map,
        'knowledge': combined_data
    }

    # Save the combined data to the output file
    with open(output_file, 'w') as output:
        json.dump(result, output, indent=4)

    print(f"Combined JSON files saved to {output_file}")
    print(f"give to the copilot AI for use as knowledge base")

# Example usage:
directory_path = '../knowledge'  # Replace with the actual directory path
output_file = '../output/combined_knowledge.json'  # Output file name
combine_json_files(directory_path, output_file)
