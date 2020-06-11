'''
Without migrations:
- We do heavy-handed work, creating and recreating the same tables in our database even for minor changes
- We can lose existing data in older tables we dropped

With migrations:
+ Auto-detects changes from the old version & new version of the SQLAlchemy models
+ Creates a migration script that resolves differences between the old & new versions
+ Gives fine-grain control to change existing tables

This is much better, because:
-->We can keep existing schema structures, only modifying what needs to be modified
-->We can keep existing data
-->We isolate units of change in migration scripts that we can roll back to a “safe” db state
'''

#1) in app.py
db.create_all()


#2) to modify our models:
class Todo(db.model):
    completed = db.Column(...)


#3) Drop existing tables:
$ dropdb todoapp && createdb todoapp

#4) Recreate tables with the newly modified models:
db.create_all()
