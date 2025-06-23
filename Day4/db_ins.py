import sqlite3

conn = sqlite3.connect("db1.db")

conn.execute('''
INSERT INTO user( userid ,USERNAME , PASSWORD) VALUES (1,"ABC1","abc123"), (2,"ABC1","abc123"),(3,"ABC1","abc123"),(4,"ABC1","abc123") 
''')

conn.commit()
conn.close()