# sqliteEx03.py
import sqlite3

class SqliteDB:
    def __init__(self, dbname):
        print('생성자 출력')
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def __del__(self):
        print('소멸자 출력')
        self.cursor.close()
        self.conn.close()

    def getJoinData(self):
        sql = " select st.id, st.name, st.birth, sg.subject, sg.jumsu "
        sql += " from students st join sungjuk sg "
        sql += " on st.id = sg.id"
        result = self.cursor.execute(sql)
        return result

    def getSubQuery(self, name):
        sql = f" select * from sungjuk where id = (select id from students where name = '{name}')"
        result = self.cursor.execute(sql)
        return result

    def getJumsu(self, name):
        sql = f" select jumsu from sungjuk where id = (select id from students where name = '{name}')"
        # result = self.cursor.execute(sql)
        # return result
        mydata = self.cursor.execute(sql)
        total = 0
        cnt = 0
        for row in mydata:
            total += row[0]
            cnt += 1
        if cnt != 0:
            average = total / cnt
            print(f'총점 : {total}, 평균 : {average}')
            return (total, average)
        else:
            print('존재하지 않는 이름입니다.')

dbname = 'sqlitedb.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoinData()
for row in dataset:
    print(row)

dataset2 = mydb.getSubQuery('이문세')
for (name, subject, score) in dataset2:
    print(name, subject, score)

dataset3 = mydb.getJumsu('고아라')