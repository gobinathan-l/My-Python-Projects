import sqlite3

def connect_d():
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def insert_d(title, author, year, isbn):
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view_d():
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    con.close()
    return rows

def search_d(title="",author="",year="",isbn=""):
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    con.close()
    return rows

def delete_d(id):
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    con.commit()
    con.close()

def update_d(id, title, author, year, isbn):
    con = sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()


connect_d()
#insert_d('Webapp Hacker\'s Handbook', 'Someone', 2020, 123458)
#update_d(2, 'Webapp Hacker\'s Handbook', 'The Hacker', 2019, 123458)
#print(view_d())
#print(search_d(author='Someone'))
#delete_d(2)
