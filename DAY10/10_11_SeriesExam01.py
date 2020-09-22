# 10_11_SeriesExam01.py
import matplotlib.pyplot as plt
from pandas import Series

plt.rc('font', family='Malgun Gothic')
myindex = ['강감찬', '홍길동', '이순신', '최영']
members = Series(data=[20, 60, 80, 40], index=myindex)
print(members)

# kind는 line, bar, barh, pie, kde(커널 밀도 추정)
# rot : 눈금 rotation
# ylim : y축 상하한 값
# color : 색상 지정
# legend : 범례, label : 범례에 들어갈 문자열
# stacked : 누적 그래프
members.plot(kind='bar', color=['r', 'g', 'b', 'y'], rot=0, ylim=[0, members.max() + 20])
plt.title('학생별 국어 시험') # plot 타이틀
plt.xlabel('학생 이름') # x축 이름
plt.ylabel('점수') # y축 이름
# plt.grid(True)
ratio = 100 * members / members.sum()
print(ratio)
for idx in range(members.size):
    value = str(members[idx]) + '건'
    ratioval = f'{ratio[idx]:.1f}%'
    plt.text(x=idx, y=members[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=members[idx] / 2, s=ratioval, horizontalalignment='center')
    
meanval = members.mean()
avg = f'평균: {meanval}건'
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0, y=meanval + 1, s=avg, horizontalalignment='center')

filename = 'SeriesGraph01.png'
plt.savefig(filename)
print(filename + '파일 저장됨')
