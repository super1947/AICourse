# makeCsv01.py
'''
pandas(판다스) :
        Series(1행 또는 1열의 데이터 집합)
        DataFrame(여러 행 또는 여러 열의 데이터 집합)
        데이터 분석을 위한 패키지
        특정 데이터 읽기 쓰기(csv, excel, web...), 통계 정보, 데이터 베이스 등등
csv 파일 : comma separate value 텍스트 파일
'''

# 임의의 데이터를 만들어서 csv 파일로 기록해보기
import random
import pandas as pd
result = []
mycolumns = ('번호', '이름', '나이')
for i in range(1, 11):
    sublist = []
    sublist.append(10*i)
    sublist.append(f'김철수{i}')
    sublist.append(random.randint(20, 40))
    result.append(sublist)
# DataFrame : 2차원 형식의 표
myframe = pd.DataFrame(result, columns=mycolumns)
filename = 'result01.csv'
myframe.to_csv(filename, mode='w', encoding='utf-8')
print('finished')