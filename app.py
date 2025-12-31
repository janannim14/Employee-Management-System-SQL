import sqlite3

# Database Connection
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create Table
cursor.execute('CREATE TABLE IF NOT EXISTS staff (id INTEGER, name TEXT, role TEXT)')

# Add Employee
cursor.execute("INSERT INTO staff VALUES (101, 'Jananni', 'Support Engineer')")
conn.commit()

print("Database and Record Created!")
conn.close()
