import sqlite3 

connection_obj = sqlite3.connect('quotes.db')

cursor_obj = connection_obj.cursor()