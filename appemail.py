from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,RadioField,SelectField,BooleanField ,SubmitField
from wtforms.validators import DataRequired,Email

app = Flask(__name__)
app.secret_key = 'emailvalidation' 

class RegistrationForm(FlaskForm):
    name= StringField("Full name", validators=[DataRequired()])
    email= StringField("Email", validators=[DataRequired(),Email()])
    password= StringField("Password", validators=[DataRequired()])
    gender= RadioField("Gender", choices=[('M','Male'),('F','Female')])
    country= SelectField("Country", choices=[('np','Nepal'),('in','India')])
    agree =BooleanField("I accept the terms and conditions", validators=[DataRequired()])
    submit =SubmitField('Register')
    
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        country = form.country.data
        # You might want to save this data to a database

        return(f"Thank you {name} From {country}, your registration is successful!")
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)