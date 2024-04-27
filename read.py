import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password'
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a new database named 'your_database'
database_name = 'your_database'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Database '{database_name}' created successfully.")
