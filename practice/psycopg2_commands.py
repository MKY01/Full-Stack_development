'''
psycopg2 commands

https://www.psycopg.org/docs/usage.html

Warning NEVER use Python string concatenation (+) or string parameters interpolation (%) to pass variables to a SQL query string.
Not even at gunpoint!!!
'''

#Establish a connection, starting a session, begins a transaction
conn = psycopg2.connect("dbname=? user=postgres")


#Sets a cursor to begin executing commands
cur = conn.cursor()
cursor = conn.cursor()


#Execute a command: this creates a new table
cur.execute("CREATE TABLE ? (id serial PRIMARY KEY, num integer, data varchar);")


#Pass data to fill a query placeholders and let Psycopg perform
#the correct conversion (no more SQL injetions!)
cur.execute("INSERT INTO ? (int, data, string, date) VALUES (%s, %s, %s, %s)"), (100, "abc'def", "foobar", '27-05-2020'))


#Query the database and obtain data as Python objects
cur.execute("SELECT * FROM ?;")

cur.fetchall() #returns all items
cur.fetchmany(3) #3 can be any integer = the number of items to fetch
cur.fetchone(1, 100, "abc'def") #fetches the first result in the result set


#Make the changes to the database persistent
cur.commit() #commit the transaction (not automatically)
conn.commit()


#Revert the last change made to the database
cur.rollback() #rollback the transaction


#Close communication with the database
cur.close()
conn.close() #close the connection (not done automatically)
