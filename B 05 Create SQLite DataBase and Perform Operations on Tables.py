import sqlite3

def display_rows(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Connect to the database or create it
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create the 'emp' table
cursor.execute("""
CREATE TABLE emp
(empno INTEGER PRIMARY KEY,
empname TEXT, salary REAL,
department TEXT)
""")
print("Table Created")

# Insert a record
cursor.execute("INSERT INTO emp VALUES (1, 'Srikanth', 50880, '17')")
cursor.execute("INSERT INTO emp VALUES (2, 'Snigdha', 78600, '')")
cursor.execute("INSERT INTO emp VALUES (3, 'Swati', 50000, 'Admin')")
conn.commit()
print("Records inserted")

# Select and display records
cursor.execute("SELECT * FROM emp")
print("Records in the table:")
display_rows(cursor)

# Update a record
cursor.execute("UPDATE emp SET salary = 100000 WHERE empno = 1")
conn.commit()
print("Record updated")

# Select and display records after update
cursor.execute("SELECT * FROM emp")
print("Records in the table after update:")
display_rows(cursor)

# Delete a record
cursor.execute("DELETE FROM emp WHERE empno = 1")
conn.commit()
print("Record deleted")

# Select and display records after deletion
cursor.execute("SELECT * FROM emp")
print("Records in the table after deletion:")
display_rows(cursor)

# Drop the table
cursor.execute("DROP TABLE emp")
conn.commit()
print("Table dropped")

# Close the connection
conn.close()
