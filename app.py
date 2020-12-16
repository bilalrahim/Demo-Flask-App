#Flask follows the MVT (model view template) architecture.
#template logic is in the templates dir which has static html files

#imp note, if changes in css file are not updated in browser. Do full relod in browser (relod + holding shift)

from flask import Flask, render_template
from flask import session, redirect, url_for

from forms import LoginForm
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

username = "bilal"
users = [
    {"email" : "bilal@gmail.com",
     "password" : "this"
    }
]

@app.route('/signup', methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = {
            "username" : form.username.data,
            "password" : form.password.data
        }
        users.append(new_user)
    else:
        print("Error!")

    return render_template("signup.html", form = form)


@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((user for user in users if user["email"]== form.email.data and user["password"] ==form.password.data), None)
        if user is None:
            return render_template("login.html", form = form, message = "Wrong credentials! Please try again.")
        else:
            print("In the user variable : " , user)
            session["user"] = user
            return render_template("home.html", message = "Successfully logged in")
    return render_template("login.html", form = form)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('home', _scheme='https', _external=True))

@app.route('/')
#Known as view, because displays what needs to be displayed.
def home():
    form = LoginForm()
    techstack = {'backend': 'flask',
                 'frontend' : 'html,css',
                 'Dynamic Rendering' : 'Jinja2'    
                }
    if 'user' in session:
        return render_template("home.html", username = username,techstack=techstack)
    else:
        return render_template("login.html", form=form)

    
@app.route('/about')
def about():
    return render_template('about.html', username=username)
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 3000)