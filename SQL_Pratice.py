import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Show all rows with rowid
cursor.execute("""
SELECT rowid, * FROM students
""")

rows = cursor.fetchall()

print("Current records:")
for row in rows:
    print(row)

# Ask user which row to delete
row_id = int(input("\nEnter rowid to delete: "))

# Delete that row
cursor.execute("""
DELETE FROM students
WHERE rowid = ?
""", (row_id,))

# Save changes
conn.commit()

print("\nUpdated records:")

# Show updated table
cursor.execute("""
SELECT rowid, * FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()