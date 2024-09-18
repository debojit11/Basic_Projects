from pathlib import Path
from pprint import pprint
import csv
# Define the path to the Desktop directory (adjust this path if necessary)
desktop_path = Path("/Users/91763/Desktop")

# Initialize a dictionary to count file types
file_type_counts = {}

# Iterate through all files on the Desktop
for file in desktop_path.iterdir():
    if file.is_file():
        # Get the file extension (e.g., '.png', '.txt')
        ext = file.suffix.lower()
        # Update the count for this extension
        if ext in file_type_counts:
            file_type_counts[ext] += 1
        else:
            file_type_counts[ext] = 1

# Pretty print the file type counts
print("File Type Counts on Desktop:")
pprint(file_type_counts)

# save the dict to a file 

file_out = open("filecounts.txt", "a")
file_out.write(str(file_type_counts))
file_out.write("\n")  # Include a line break
file_out.close()
with open("filecounts.txt", "r") as file_in:
    print(file_in.read())


with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [file_type_counts[".lnk"], file_type_counts[".ini"], file_type_counts[".txt"], file_type_counts[".url"]]
    countwriter.writerow(data)

# analyze.py
import csv

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["LNK", "INI", "TXT", "URL"])
    counts = list(reader)

print(counts)



# Create folders for file types with more than 5 files


for ext, count in file_type_counts.items():
    if count > 5:
        # Define the folder path based on the file type
        folder_path = desktop_path / f'{ext[1:].upper()}_Files'
        folder_path.mkdir(exist_ok=True)  # Create the folder if it does not exist
        
        # Move files of this type into the folder
        for file in desktop_path.glob(f'*{ext}'):
            if file.is_file():
                file.rename(folder_path / file.name)
        print(f"Moved {count} {ext} files to {folder_path}")