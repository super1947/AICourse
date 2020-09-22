# 10_09_DataFrameExam01.py
from pandas import DataFrame
import pprint
sdata = {'도시': ['서울', '서울', '서울', '부산', '부산'],
    'year': [2000, 2001, 2002, 2001, 2000],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
print(type(sdata))
# pprint(sdata)
myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
print(type(myframe))
print(myframe)
myframe.index.name = '호호호'
myframe.columns.name = '하하하'
print(myframe.index)
print(myframe.columns)
print(myframe.values)
print(type(myframe.values))
print(myframe.dtypes)
print(myframe.T) # T : 전치 ( 2 X 3 행렬을 3 X 2로 바꾸는 행위)
mycolumns = ['pop', '도시', 'year']
newframe = DataFrame(sdata, columns=mycolumns)
print(newframe)
# print(myframe)