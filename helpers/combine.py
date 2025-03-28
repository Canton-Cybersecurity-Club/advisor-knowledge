import os
import json

def combine_files_to_json(directory_path, output_file):
    combined_data = {
        "index": [],
        "content": []
    }
    
    index_num = 0
    for filename in sorted(os.listdir(directory_path)):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                
            # Add to index
            combined_data["index"].append(f"{index_num} - {filename}")
            
            # Append file content with a header
            combined_data["content"].append({
                "id": index_num,
                "filename": filename,
                "data": content
            })
            index_num += 1
            
    # Save to JSON output file
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(combined_data, output, indent=4)  # Use indent for better readability
    
    print(f"Combined files saved to {output_file}")

