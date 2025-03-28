from helpers.combine import combine_files_to_json
from helpers.instruction_check import check_instructions

if __name__ == "__main__":
    input_file = './knowledge/instructions/instructions.md'  # Replace with the path to your input Markdown file
    output_directory = './output'  # Replace with your desired output directory
    check_instructions(input_file, output_directory)
    
    directory_path = './knowledge/sections'  # Replace with the actual directory path
    output_file = './output/output_combined_knowledge.json'  # Output file name
    combine_files_to_json(directory_path, output_file)

else:
    print("Script imported as module")