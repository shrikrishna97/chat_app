import sqlite3
conn = sqlite3.connect("data.db",check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tablem(date DATE UNIQUE, message STRING, user STRING) ")
def add_data(date,sale,purchase,current):
    c.execute("INSERT INTO tablem(date,message,user) VALUES (?,?,?,?)",(date,message,user))
    conn.commit()
def view_all():
    c.execute("SELECT * FROM tablem")
    data = c.fetchall()
    return data
# def delete_data(date):
# 	c.execute('DELETE FROM tablem WHERE date="{}"'.format(date))
# 	conn.commit()         
# def view_current(date):
#     c.execute('SELECT current_money FROM tablem WHERE date="{}"'.format(date))
#     f = c.fetchone()
#     return f   
