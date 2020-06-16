#Delete

##In SQL:

DELETE FROM table_name
WHERE condition;


##In SQLAlchemy ORM:

todo = Todo.query.get(todo_id)
db.session.delete(todo) # or...
Todo.query.filter_by(id=todo_id).delete()
db.session.commit()
