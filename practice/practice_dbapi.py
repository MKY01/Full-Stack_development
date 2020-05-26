import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cur = connection.cursor()

cur.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

connection.commit()

connection.close()

cursor.close()