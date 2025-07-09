from flask import Flask, request,render_template
import sqlite3

app = Flask(__name__) 

def init_db():
    conn =sqlite3.connect('users.db')
    cursor =conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("prasanna", "prasanna123"))
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        qurey= f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(qurey)
        user = cursor.fetchone()
        conn.close()

        if user:
            message = "Login successful!"
        else:
            message = "Login failed!"

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
