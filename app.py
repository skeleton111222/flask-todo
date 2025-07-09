from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    error=None
    if request.method=='POST':
        name=request.form['name'].strip()
        if not name:
            error="Name cannot be empty!"
        else:
            return f"Hello,{name}!"
    return render_template('indexx.html',error=error)

if __name__=="__main__":
    app.run(debug=True,port=5000)
