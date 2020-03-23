import sqlite3

def create_t():
    con = sqlite3.connect("sql.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, cost REAL)")
    con.commit()
    con.close()

def insert_t(item, quantity, cost):
    con = sqlite3.connect("sql.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, cost))
    con.commit()
    con.close()

def view_t():
    con = sqlite3.connect("sql.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete_t(item):
    con = sqlite3.connect("sql.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item = ?",(item,))
    con.commit()
    con.close()



delete_t("wine")
print(view_t())
