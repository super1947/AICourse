# sqliteEx01.py
# sqlite : 소형 개인용 데이터 저장을 위한 데이터 베이스

import sqlite3 # sqlite를 위한 모듈
# conn : 데이터 베이스에 접근하기 위한 객체
# database : 데이터 베이스 파일 이름
conn = sqlite3.connect(database='sqlitedb.db')
print(type(conn))
print('finished')

# cursor(커서) : 데이터 베이스 작업을 수행하고 있는 메모리 공간
mycursor = conn.cursor()
try:
    mycursor.execute("drop table students") # execute함수 : sql 구문을 실행해주는 함수
except sqlite3.OperationalError as err:
    print(err)
mycursor.execute("create table students(id text primary key, name text, birth text)")
sql = "insert into students(id, name, birth) values('lee', '이승기', '1989/12/15')"
mycursor.execute(sql)
sql = "insert into students(id, name, birth) values('kang', '강감찬', '1234/12/20')"
mycursor.execute(sql)
datamylist = [('jo', '조인성', '1984/03/14'), ('ko', '고아라', '1988/05/24'), ('sim', '심형래', '1964/11/05'), ('park', '박지성', '1981/06/07')]
# ? : place holder라고 함. 치환되어야 할 어떤 값
# 데이터 유형에 상관없이 외따옴표 적지 마라
sql = "insert into students(id, name, birth) values(?, ?, ?)"
mycursor.executemany(sql, datamylist)
findID = 'ko'
sql = f"select * from students where id = '{findID}'"
mycursor.execute(sql)
result = mycursor.fetchone()
if result != None:
    print(f"아이디 : {result[0]}")
    print(f'이름 : {result[1]}')
    print(f'생일 : {result[2]}')
else:
    print('문제가 있습니다.')
sql = "select * from students order by name DESC"
for id, name, birth in mycursor.execute(sql):
    print(f'{id} # {name} # {birth}')

sql = "SELECT * from students where name like '%이%'"
mycursor.execute(sql)
print(mycursor.fetchall())

# id 가 lee인 친구의 이름을 '이문세'로 바꾸세요.
sql = "update students set name = '이문세' where id = 'lee'"
mycursor.execute(sql)
# id 가 sim인 친구의 데이터를 삭제하세요.
sql = "delete from students where id = 'sim'"
mycursor.execute(sql)

sql = "select * from students order by name"
for id, name, birth in mycursor.execute(sql):
    print(f'{id}, {name}, {birth}')

conn.commit()
mycursor.close()
conn.close()

# SELECT * from students;
# SELECT * from students where id = 'ko';
# select * from students order by name DESC;
# SELECT * from students where name like '%이%';