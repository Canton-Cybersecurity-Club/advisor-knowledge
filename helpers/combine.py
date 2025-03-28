import os

def combine_files(directory_path, output_file):
    combined_content = []
    index_section = ["# Index\n"]
    
    # Loop through all files in the directory
    index_num = 0
    for filename in sorted(os.listdir(directory_path)):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                
            # Add to index
            
            index_section.append(f"{index_num} - {filename}\n")
            
            # Append file content with a header
            combined_content.append(f"\n# {index_num} - {filename}\n\n ``` \n {content} \n ```")
        index_num += 1
    # Combine all sections
    final_output = "\n".join(index_section) + "\n" + "\n".join(combined_content)
    
    # Save to output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(final_output)
    
    print(f"Combined files saved to {output_file}")
