import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS table2;")


cur.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')


#method 1 - passing in as a string composition as a tuple
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1,True))


#method 2 - SQL using a template and data variable as a dictionary
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False,

    'id': 3,
    'completed': False,
}

cursor.execute(SQL, data)

cursor.execute('SELECT * from table2;')

result = cursor.fetchone()
print('fetchone', result)

result2 = cursor.fetchmany(2)
print('fetchmany(2)', result2)

result3 = cursor.fetchall()
print('fetchall', result3)



connection.commit()

connection.close()
cursor.close()
