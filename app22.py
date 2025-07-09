from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'komal123'

@app.route('/')
def index():
    if 'user' in session:
        return f"Hello {session['user']}! <a href='/logout'>Logout</a> | <a href='/transfer'>Transfer Money</a>"
    return "<a href='/login'>Login</a>"

@app.route('/login')
def login():
    session['user'] = 'Komal'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return "Unauthorized", 401

    if request.method == 'POST':
        to = request.form['to']
        amount = request.form['amount']
        return f"{amount} transferred to {to} by {session['user']}!"

    return '''
        <form method="POST">
            Send To: <input name="to"><br>
            Amount: <input name="amount"><br>
            <button type="submit">Transfer</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)