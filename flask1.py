from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        # Handle GET request
        return render_template('index.html')
    elif request.method == 'POST':
        # Handle POST request (e.g., form submission)
        # You can process form data here
        # For example:
        # name = request.form.get('name')
        # return f"Received name: {name}"
        return "Received a POST request!"
    else:
        # Optional: handle other methods if needed (should not happen unless specified)
        return "Method not allowed", 405

# Other routes remain unchanged

@app.route('/htmls')
def hellooo():
    return render_template('boot.html')

@app.route('/message')
def message():
    return "Hello, World!"

@app.route('/pizza')
def pizza():
    return render_template('pizza.html')

@app.route('/ncit')
def ncit():
    return render_template('ncit.html')

if __name__ == '__main__':
    app.run(debug=True, port=1000)