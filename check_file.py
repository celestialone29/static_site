import os

file_path = 'content/majesty/index.md'

# Check if the file exists
if os.path.isfile(file_path):
    print("The file exists!")
else:
    print("The file does not exist.")
