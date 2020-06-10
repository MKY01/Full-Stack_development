'''
Pattern (try-except-finally)
'''

import sys

try:
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
except:
  db.session.rollback()
  error=True
  print(sys.exc_info())
finally:
  db.session.close()
