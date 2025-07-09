from flask import Flask , render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)

app.config['SQLLACHEMY_DATABASE_URL'] = 'sqlite:///group.db'
app.config['SQLALCHEMY_TRACK_NOTIFYING'] = False

db = SQLALchemy(app)

class Student(db.model):
    id = db.coloum(db.Integer, primary_key=True)
    name = db.coloumn(db.String[100],nullable=False)
    email = db.coloumn(db.String[100],unique=True ,nullable=False)

@app.route('/add')
def add_student():
    student = Student(name='Lujan',email='lujan1@gmail.com')
    db.session.add(student)
    db.session.commit()
    return 'Student added to our database'

@app.route('/student')
def list_student():
    students = Student.query.all()
    return '<br>'.join([f'{s.id}.{s.name} - {s.email}' for s in students])

@app.route('/') 
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)