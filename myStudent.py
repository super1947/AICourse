# myStudent.py
from xml.etree.ElementTree import parse
from pandas import DataFrame

tree = parse('mystudent.xml')
myroot = tree.getroot()
allstudent = myroot.findall('student')
# print(allstudent)
mylist = []
for person in allstudent:
    name = person.find('name')
    korean = person.find('국어')
    english = person.find('영어')
    math = person.find('수학')
    total = int(korean.text) + int(english.text) + int(math.text)
    avg = total / (len(person) - 1)
    sublist = [name.text, korean.text, english.text, math.text, total, avg]
    mylist.append(sublist)
print(mylist)
mycolumns = ['name', '국어', '영어', '수학', '총점', '평균']
myframe = DataFrame(mylist, columns=mycolumns)
filename = 'student.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)

filename = 'student.csv'
myfile = open(file=filename, mode='r', encoding='utf-8')
mylist = [item.strip().split(',') for item in myfile.readlines()]
print(mylist)

import sqlite3
conn = sqlite3.connect('students.db')
mycursor = conn.cursor()
mycursor.execute("create table students(name text, 국어 text, 영어 text, 수학 text, 총점 text, 평균 text)")
sql = "insert into students (name, 국어, 영어, 수학, 총점, 평균) values(?, ?, ?, ?, ?, ?)"
mycursor.executemany(sql, mylist)
conn.commit()
mycursor.close()
conn.close()