'''
this file must be named 'app.py' or flask wont run!
To run you will have to cd into the location of the flask app, then run it by the following temrinal command:
FLASK_APP=app.py FLASK_DEBUG=true flask run
'''


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])
