import mysql.connector
from datetime import datetime

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",      
    user="your_mysql_user",  
    password="your_password",  
    database="desktop_stats"   
)
cursor = conn.cursor()

# Calculate the total number of files tracked
cursor.execute("SELECT SUM(count) FROM file_counts")
total_files = cursor.fetchone()[0]

# Calculate the total number for each file type
cursor.execute("SELECT ext, SUM(count) FROM file_counts GROUP BY ext")
total_per_file_type = cursor.fetchall()

# Find the day with the most items on the desktop
cursor.execute("""
    SELECT run_time, SUM(count) as total_files
    FROM file_counts
    GROUP BY DATE(run_time)
    ORDER BY total_files DESC
    LIMIT 1
""")
most_items_day = cursor.fetchone()

# Find the most common file type ever on the desktop
cursor.execute("""
    SELECT ext, SUM(count) as total
    FROM file_counts
    GROUP BY ext
    ORDER BY total DESC
    LIMIT 1
""")
most_common_file_type = cursor.fetchone()

# Print the results
print(f"Total number of files tracked: {total_files}")
print("Total number of each file type:")
for ext, total in total_per_file_type:
    print(f"File Type: {ext}, Total: {total}")

print(f"Day with the most items: {most_items_day[0]} ({most_items_day[1]} files)")
print(f"Most common file type: {most_common_file_type[0]} ({most_common_file_type[1]} files)")

# Create (or update) analysis table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (
        id INT AUTO_INCREMENT PRIMARY KEY,
        total_files INT,
        most_items_day DATE,
        most_common_file_type VARCHAR(10),
        analysis_time DATETIME
    )
""")

# Insert analysis result into the analysis table
analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("""
    INSERT INTO analysis (total_files, most_items_day, most_common_file_type, analysis_time)
    VALUES (%s, %s, %s, %s)
""", (total_files, most_items_day[0], most_common_file_type[0], analysis_time))

# Commit and close connection
conn.commit()
conn.close()
print("Analysis results saved to the MySQL database.")