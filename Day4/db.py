import sqlite3

conn = sqlite3.connect('db1.db')
conn.execute('''
create table user(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME VARCHAR(100),
    PASSWORD VARCHAR(100))
    
    ''')

conn.close