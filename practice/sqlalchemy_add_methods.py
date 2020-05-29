'''
SQLAlchemy insert new records into the database
'''

#$ cd to my directory
#$ python3

from app import db, Person

#INSERT
person1 = Person(name='Kit')
db.session.add(person)
db.session.add_all([person1, person2])

#UPDATE
person2.name = 'Maria'

#DELETE
db.session.delete(person2)

db.session.commit()

person1.name


#export FLASK_DEBUG=True
#flask run
