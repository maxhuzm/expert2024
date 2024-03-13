import sqlite3

connect = sqlite3.connect("baza.sqlite")
curs = connect.cursor()
zapros = "select "