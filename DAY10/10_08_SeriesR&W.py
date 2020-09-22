# 10_08_SeriesR&W.py
from pandas import Series
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

myindex = ['서울', '부산', '광주', '대구', '울산', '목포', '여수']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print(myseries['대구'])
print(type(myseries['대구'])) # type : numpy
print(myseries[['대구']])
print(type(myseries[['대구']])) # type : Series
print(myseries['대구':'목포']) # 문자열 색인으로 슬라이싱 하는 경우 양쪽 모두 포함됨
print(myseries[[2]]) # 인덱싱 할 때 대괄호 2개
print(myseries[0:5:2]) # 콜론으로 슬라이싱 하는 경우 대괄호 1개
print(myseries[[1, 3, 5]]) # 콤마를 사용하는 경우 대괄호 2개
myseries[2:5] = 33
print(myseries)
myseries[['서울', '대구']] = 44
print(myseries)
myseries[0::2] = 77
print(myseries)

colors=['r', 'g', 'b', 'y', 'royalblue', 'c', 'm']
myseries.plot(kind='bar', rot=0, color=colors)
plt.xlabel('도시')
plt.ylabel('점수')
ratio = 100 * myseries / myseries.sum()
for idx in range(myseries.size):
    value = str(myseries[idx])
    ratioval = f'{ratio[idx]:.1f}%'
    plt.text(x=idx, y=myseries[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=myseries[idx] / 2, s=ratioval, horizontalalignment='center')
graphfile = 'SeriesR&W_Graph.png'
plt.savefig(graphfile)