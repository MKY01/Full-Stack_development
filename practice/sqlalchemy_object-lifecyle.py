'''
SQLAlchemy Object lifecycle stages
'''

#1. Transient - define an object.
person = Person(name='Amy')
widget = Widget(name='foo')

#2. Pending - attach an object to the session, update it or undo it.
db.session.add(person)
db.session.all_all()
person.name = 'Mary'
db.session.delete(user)
db.session.rollback()

#3. Flushed - Push changes: Python --> SQL expressions(engine) @buffer If autocommit == true, it will commit.
db.session.flush()

Person.query.all() #calling query 'flushes' pending changes! Cache it, but still not yet in the database.

#4 Commited - (2-step-in-1) call for a change to persist in the database, clear the transaction.
db.session.commit()

#5 Merge - in-memory objects to be synchronised with each other
db.session.merge(user)
