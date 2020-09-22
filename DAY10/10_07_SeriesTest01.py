# 10_07_SeriesTest01.py
from pandas import Series

# Series : 1차원적인 동일한 타입의 데이터 묶음
# 엑셀 파일의 특정한 1개의 컬럼 정보

# 색인을 지정하지 않으면, 0부터 순차적으로 숫자를 매긴다.
mylist = [10, 40, 30, 20]
myseries = Series(mylist)
print(myseries)

# 색인을 지정하려면, index 매개 변수를 사용
myseries = Series(mylist, index=['강감찬', '이순신', '김유신', '광해군'])
print(type(myseries))
print(myseries)

# 색인에 이름 지정하기
myseries.index.name = '이름'
print(myseries)

myseries.name = '학생들 시험'
print(myseries)