import sqlite3
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

# Function to establish a new SQLite connection
def get_db_connection(a):
    conn = sqlite3.connect(a)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    conn = get_db_connection('database.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    c.execute(query)
    user = c.fetchone()
    conn.close()
    if user:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password.'})

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = c.fetchone()
    if existing_user:
        conn.close()
        return jsonify({'success': False, 'message': 'Username already exists.'})
    else:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return jsonify({'success': True})

@app.route('/home')
def home():
     return render_template('home.html')
     
# Add a new route to submit comments
@app.route('/submit_comment', methods=['POST'])
def submit_comment():
        comment_text = request.form['comment']
        # Save the comment to the database (you need to modify your database schema and code accordingly)
        # For example:
        conn = get_db_connection('comments.db')
        c = conn.cursor()
        c.execute("INSERT INTO comments (text) VALUES (?)", (comment_text,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Comment submitted successfully.'})

# Add a new route to fetch comments
@app.route('/get_comments', methods=['GET'])
def get_comments():
    # Retrieve comments from the database (modify this according to your database schema)
    # For example:
     conn = get_db_connection('comments.db')
     c = conn.cursor()
     c.execute("SELECT * FROM comments")
     comments = [{'text': row['text']} for row in c.fetchall()]
     conn.close()
     return jsonify(comments)
    # For demonstration, let's return dummy comments
 #   dummy_comments = [{'text': 'Dummy comment 1'}, {'text': 'Dummy comment 2'}]
  #  return jsonify(dummy_comments)     

if __name__ == '__main__':
    app.run(debug=True)