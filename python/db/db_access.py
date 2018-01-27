try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

db_connection = sqlite.connect('sample.db')

db_curs = db_connection.cursor()
try:
    db_curs.execute('DROP TABLE people')
except sqlite3.OperationalError:
    print('Deleting a table that did not exist')

db_curs.execute("CREATE TABLE people (\
    id INTEGER PRIMARY KEY, first_name VARCHAR(20),\
    last_name VARCHAR(30), date_of_birth DATE)")
db_curs.execute("INSERT INTO people (first_name, last_name, date_of_birth)\
    VALUES ('Arun', 'Panayappan', '2018-1-2')")


db_connection.commit()

db_curs.execute("SELECT * FROM people")
print('From Database:',db_curs.fetchall())


#Parameterized statements
stmt = "INSERT INTO people (first_name, last_name, date_of_birth) VALUES (?,?,?)"
db_curs.execute(stmt, ('Radha', 'Manivasagam', '2018-1-2'))
db_curs.execute(stmt, ('Norman', 'Parkinson', '1913-4-21'))

db_curs.execute("SELECT * FROM people")
print(db_curs.fetchall())


stmt = "UPDATE people\
            SET first_name='Arun'\
            WHERE first_name='Radha'"
db_curs.execute(stmt)

db_curs.execute("SELECT * FROM people")
print(db_curs.fetchall())
