'''
Writing SQLAlchemy vs raw SQL - creating a todos table


CREATE TABLE todos(
    id INTEGER PRIMARY KEY,
    description VARCHAR NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT false
);
'''

class Todo(db.model):
    """docstring for ORM."""
    id = db.column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False default=False)

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
