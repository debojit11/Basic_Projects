# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib
jpg_files_path = pathlib.Path('/Users/91763/Pictures')
file_paths = []

for file in jpg_files_path.rglob('*'):
    if file.is_file():
        file_paths.append(str(file))

formatted_output = '[\n' + ',\n'.join(f'  "{path}"' for path in file_paths) + '\n]'
print(formatted_output)


file_extensions = []

for file in jpg_files_path.rglob('*'):
    if file.is_file():
        ext = file.suffix.lower()
        if ext and ext not in file_extensions:
            file_extensions.append(ext)


formattedd_output = '[\n' + ',\n'.join(f'  "{ext}"' for ext in file_extensions) + '\n]'
print(formattedd_output)
