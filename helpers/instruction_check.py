import os
import shutil

def process_markdown_file(input_file, output_directory):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
    
    # Read the content of the Markdown file
    with open(input_file, 'r') as file:
        content = file.read()

    # Check the character count
    char_count = len(content)
    print(f"Character count: {char_count}")

    # If the character count is under 8,000, save a copy to the output directory
    if char_count < 8000:
        # Get the base filename and create the output path
        base_filename = os.path.basename(input_file)
        output_path = os.path.join(output_directory, base_filename)

        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Save the file to the output directory
        with open(output_path, 'w') as output_file:
            output_file.write(content)
        
        print(f"File successfully saved to {output_path}")
    else:
        print("The file exceeds 8,000 characters and was not saved.")

# Example usage:
input_file = '../knowledge/instructions.md'  # Replace with the path to your input Markdown file
output_directory = '../output'  # Replace with your desired output directory
process_markdown_file(input_file, output_directory)
