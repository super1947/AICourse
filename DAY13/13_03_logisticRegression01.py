# 13_03_logisticRegression01.py
# 카페 https://cafe.naver.com/ugcadman/1113 아이리스 데이터셋
import pandas as pd
from sklearn.model_selection import train_test_split
filename = 'iris.csv'
data = pd.read_csv(filename)

x_data = data[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y_data = data[['Name']]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7)
'''
데이터 속성들의 값의 차이가 너무 크면 학습이 잘 안되므로
StandardScaler 클래스를 사용하여 평균 0, 표준편차 1인 정규 분포로 표준화를 수행
정확도 구하기(confusion matrix 및 각 지표에 대한 확인)
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)
train_score = model.score(x_train, y_train)
print(f'train 정확도: {train_score:.3f}')
train_score = model.score(x_test, y_test)
print(f'train 정확도: {train_score:.3f}')
print('회귀 계수')
print(model.coef_)
print(model.intercept_)

from sklearn.metrics import confusion_matrix
print('test result')
prediction = model.predict(x_test)
# confusion_matrix(정답데이터, 예측데이터)
cf_matrix = confusion_matrix(y_test, prediction)
print('confusion matrix')
print(cf_matrix)

from sklearn.metrics import accuracy_score
# accuracy_score : 정확도를 구해주는 함수
accuracy = accuracy_score(y_test, prediction)
print(f'accuracy : {accuracy*100:.3f}%')

from sklearn.metrics import  classification_report
# 주요 분류와 관련된 metrics(지표)에 대한 보고서
cl_report = classification_report(y_test, prediction)
print(cl_report)

# HeatMap 그리기
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
sns.heatmap(pd.DataFrame(cf_matrix), annot=True, cmap='YlGnBu', fmt='g')
plt.title('confusion matrix')
plt.ylabel('actual label')
plt.xlabel('prediction label')
filename = 'logisticRegression01.png'
plt.savefig(filename)

