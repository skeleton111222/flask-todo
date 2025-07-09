from flask import Flask, session, render_template

app = Flask(__name__)

app.secret_key='Prasanna'

###### Setting a session ########

@app.route('/login')
def login():
    session['username']='Prasanna Shakya'
    return 'Logged in'

########## Accessing a session ########
@app.route('/profile')
def profile():
    username = session.get('username')
    return f'Logged in as {username}'

############ Removing a cookies ######
@app.route('/logout')
def logout():    
    session.pop('username',None)
    return 'Logged out!'

@app.route('/')
def index():
    return render_template('indexcookie1.html') 

if __name__ == '__main__':
    app.run(debug=True)

# Example:
# Cookies:
# Imagine you visit an online store. A cookie might be stored in your browser to remember 
# your shopping preferences (e.g., currency, language) or to keep track of whether you have agreed to a website’s privacy policy.

# Sessions:
# When you log into that same online store, the server creates a 
# session to keep track of your logged-in status and any actions (like items in a shopping cart).
# The server stores the data, and your browser holds a session ID, which tells the server who you are.

# Cookies store data on the client-side (browser), while sessions store data on the server-side.
#  Key Differences Between Cookies and Sessions:
# Where the Data is Stored:

# Cookies: Stored on the client’s browser.
# Sessions: Stored on the server, with a session ID saved in the client’s browser.

# Security:

# Cookies: Less secure, as data is stored on the client-side and can be tampered with.
# Sessions: More secure, as data is stored on the server-side and only the session ID is shared with the client.

# Size of Data:

# Cookies: Limited to about 4 KB of data.
# Sessions: No size limit, as data is stored on the server.

# Expiration:

# Cookies: Can have a fixed expiration (e.g., hours, days, or browser session).
# Sessions: Expire after inactivity or when the user logs out.