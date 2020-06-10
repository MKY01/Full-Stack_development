'''
this file must be named 'app.py' or flask wont run!
To run you will have to cd into the location of the flask app, then run it by the following terminal command:
FLASK_APP=app.py FLASK_DEBUG=true flask run
I have to manually create a PostgreSQL database by create todoapp
then inserted some dummy data into the columns
INSERT INTO todos (description) VALUES ('Do a thing 1');
INSERT INTO todos (description) VALUES ('Do a thing 2');
INSERT INTO todos (description) VALUES ('Do a thing 3');
INSERT INTO todos (description) VALUES ('Do a thing 4');
'''


from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'description': todo.description
    })

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all()
    )
