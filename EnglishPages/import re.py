import os
import re

# Define the folder path
folder_path = r"c:\Users\user\mama\github.io"

# Function to remove comments from a file
def remove_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Remove CSS/JS comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Walk through the folder and process files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(('.html', '.css', '.js')):  # Process only HTML, CSS, and JS files
            file_path = os.path.join(root, file)
            remove_comments(file_path)

print("All comments have been removed from the folder.")