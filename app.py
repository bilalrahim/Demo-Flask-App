#Flask follows the MVT (model view template) architecture.
#template logic is in the templates dir which has static html files

#imp note, if changes in css file are not updated in browser. Do full relod in browser (relod + holding shift)


from flask import Flask, render_template
app = Flask(__name__)


username = "Bilal"
@app.route('/')
#Known as view, because displays what needs to be displayed.
def home():
    techstack = {'backend': 'flask',
                 'frontend' : 'html,css',
                 'Dynamic Rendering' : 'Jinja2'    
                }
    return render_template("home.html", username = username,techstack=techstack)

@app.route('/about')
def about():
    return render_template('about.html', username=username)
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 3000)