from flask import Flask, render_template, request

app = Flask(__name__)

# Store comments in-memory (just for this example)
comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)  # Add the user's comment to the list
    return render_template('indexxss.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
