# 10_10_DataFrameR&W01.py
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

mylist = [10*onedata for onedata in range(1, 26)]
print(mylist)
myindex = ['손흥민', '박지성', '황희찬', '이승우', '이영표']
mycolumns = ['영국', '네덜란드', '독일', '벨기에', '한국']

myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)
print(type(myframe))

# iloc : i행의 값을 series로 리턴
result = myframe.iloc[1]
print(result)
print(type(result))

result = myframe.iloc[[1, 3]] # 대괄호 2개면 DataFrame으로 리턴
print(result)
print(type(result))

result = myframe.iloc[::2]
print(result)
print(type(result))

# loc : loc는 location
result = myframe.loc[['박지성']] # DataFrame 으로 리턴
print(result)
print(type(result))

result = myframe.loc['박지성'] # Series로 리턴
print(result)
print(type(result))

# 황희찬과 이영표 출력
result = myframe.loc[['황희찬', '이영표']]
print(result)
print(type(result))

#                       행        행         열        열
result = myframe.loc[['이승우', '이영표'], ['영국', '벨기에']] 
print(result)
print(type(result))

result = myframe.loc['박지성':'이승우', '네덜란드':'벨기에']
print(result)
print(type(result))

result = myframe.loc[[False, True, True, False, True]]
print(result)
print(type(result))

print(myframe['영국'] <= 100)
result = myframe.loc[myframe['영국'] <= 100]
print(result)
print(type(result))

# print(myframe.loc[myframe['벨기에'] == 140])

# 네덜란드 70이상이고, 벨기에 140 이상인 항목
# all(), any() 함수를 사용하는 예시
con1 = myframe['네덜란드'] >= 70
con2 = myframe['벨기에'] >= 140
print(con1)
print(con2)
df = DataFrame([con1, con2])
print(df)
print(df.all())
print(df.any())

result = myframe.loc[df.all()]
print(result)

result = myframe.loc[df.any()]
print(result)

# lambda 입력 매개 변수 : 함수 내용(하고자 하는 일)
aa = lambda x: x + 3
print(aa(10))

result = myframe.loc[lambda df: df['독일'] >= 130]
print(result)

myframe.loc[['손흥민', '황희찬'], ['네덜란드']] = 30
print(myframe)

myframe.loc['박지성':'이승우', ['네덜란드']] = 80
print(myframe)
myframe.loc['이영표', :] = 55
print(myframe)
myframe.loc[:, ['독일']] = 60
print(myframe)

myframe.plot(kind='bar')
graphfile = 'DataFrameR&W_Graph.png'
plt.savefig(graphfile)
