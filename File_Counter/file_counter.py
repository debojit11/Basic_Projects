# Add the code for the file counter script that you wrote in the course.
from pathlib import Path
from datetime import datetime
import mysql.connector

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

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",      # Adjust if necessary
    user="root",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="desktop_stats"   # Replace with your database name
)
cursor = conn.cursor()

# Create a table to store file counts (if it doesn't already exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_counts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        run_time DATETIME,
        ext VARCHAR(10),
        count INT
    )
""")

# Insert file type counts with timestamp into the database
run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for ext, count in file_type_counts.items():
    cursor.execute("INSERT INTO file_counts (run_time, ext, count) VALUES (%s, %s, %s)", 
                   (run_time, ext, count))

# Commit the transaction and close the connection
conn.commit()
conn.close()
print("File counts saved to the MySQL database.")
