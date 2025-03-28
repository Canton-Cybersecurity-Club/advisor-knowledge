import os

def combine_md_files(directory_path, output_file):
    combined_content = []
    index_section = ["# Index\n"]
    
    # Loop through all files in the directory
    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith('.md'):  # Check if the file is a Markdown file
            file_path = os.path.join(directory_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Add to index
            index_section.append(f"- [{filename}](#{filename.replace('.md', '').replace(' ', '-').lower()})")
            
            # Append file content with a header
            combined_content.append(f"\n# {filename}\n\n" + content)
    
    # Combine all sections
    final_output = "\n".join(index_section) + "\n" + "\n".join(combined_content)
    
    # Save to output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(final_output)
    
    print(f"Combined Markdown files saved to {output_file}")

# Example usage:
directory_path = '../knowledge'  # Replace with the actual directory path
output_file = '../output/combined_knowledge.md'  # Output file name
combine_md_files(directory_path, output_file)
