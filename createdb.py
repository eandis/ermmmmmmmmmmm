import sqlite3

# Define a function to create the database tables
def create_comments_table():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 text TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Call the function to create the comments table
create_comments_table()

# Call the function to create tables
create_tables()