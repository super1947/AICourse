# sqliteEx02.py
import sqlite3
conn = sqlite3.connect(database='sqlitedb.db')

mycursor = conn.cursor()
try:
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError as err:
    print(err)
mycursor.execute("create table sungjuk(id text, subject text, jumsu integer)")
mydatalist = [('lee', 'java', 10), ('lee', 'html', 20), ('lee', 'python', 30), ('jo', 'java', 40), ('jo', 'html', 50), \
              ('jo', 'python', 60), ('ko', 'java', 70), ('ko', 'html', 80), ('ko', 'python', 90)]
sql = "insert into sungjuk(id, subject, jumsu) values(?, ?, ?)"
mycursor.executemany(sql, mydatalist)
conn.commit()
mycursor.close()
conn.close()