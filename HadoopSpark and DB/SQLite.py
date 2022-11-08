#.venv/Scripts/activate
#sqlite for windows - https://www.youtube.com/watch?v=XA3w8tQnYCA
#./sqlite3 books.db -init books.sql

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))
print(pd.read_sql('SELECT * FROM author_ISBN', connection))
print(pd.read_sql('SELECT * FROM titles', connection))
print(pd.read_sql('SELECT first, last FROM authors WHERE id = 1', connection))
print(pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection))
print(pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id']))
print(pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id']))
print(pd.read_sql('SELECT title FROM titles ORDER BY title DESC', connection))
print(pd.read_sql("""SELECT id, first, last  FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id']))
print(pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title DESC""", connection))
print(pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head())

#Insert
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print(cursor.rowcount)
cursor = cursor.execute('DELETE FROM authors WHERE id=6') 
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
connection.close()