#had to seperate our application module "app.py" from forms module.

from flask_wtf import FlaskForm

#importing the required classes needed for fields.
from wtforms import PasswordField, StringField, SubmitField
#importing the required validators.
from wtforms.validators import InputRequired

#For each form in our app we will create a class.
#Now for our login form we create the below class that inherits FlaskForm
""" 
For each possible field, wtforms has associated classes. For this particular example we will only import the fields we need.
StringField for an email
PasswordField for a password
SubmitField for the submit button
"""

class LoginForm(FlaskForm):

    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    
    submit = SubmitField("Login")
# we will make instances of these classes as member variables of our class, 
# and we will pass the labels of these fields as input to the constructors


#Class for signup form.

class SignupForm(FlaskForm):
    password = PasswordField("Password", validators = [InputRequired()])
    username = StringField("Email", validators =[InputRequired()])
    
    submit = SubmitField('Sign up')

    