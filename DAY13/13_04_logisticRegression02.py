# 13_04_logisticRegression02.py
import pandas as pd
filename = 'titanic.csv'
data = pd.read_csv(filename)
print(data.columns)

# 코딩 변경 : 데이터 분석에 맞게 사용자가 값을 변경하는 작업
print(data['Sex'].unique()) # unique() : 중복된 데이터는 배제하고 1개만 표시
data['Sex'] =data['Sex'].map({'female': 1, 'male': 0})
print(data['Sex'].unique())

# 결측치(missing value) : 누락된 데이터, 출력 결과에 nan으로 표시
# print(data['Age'].unique())
# 결측치에 대하여 나머지 항목들의 평균 값으로 치환함
data['Age'].fillna(value=data['Age'].mean(), inplace=True)
print(data['Age'].unique())

print(data['Pclass'].unique())
result = data.groupby('Pclass')['Pclass'].count()
print('좌석 등급별 인원 수')
print(result)
# FirstClass 컬럼에는 Pclass의 값이 1일때만 1을, 나머지는 0으로 채운다.
data['FirstClass'] = data['Pclass'].apply(lambda x: 1 if x == 1 else 0)
# SecondClass 컬럼에는 Pclass의 값이 2일때만 1을, 나머지는 0으로 채운다.
data['SecondClass'] = data['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# 성별, 나이, 일등석/이등석 정보를 이용하여 생존 여부 파악하기
x_data = data[['Sex', 'Age', 'FirstClass', 'SecondClass']]
y_data = data[['Survived']]

# 데이터 셋 분리 작업
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7)

# 정규화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

# fit_transform 함수를 사용하여 이미 한번 fit 했으므로
# 두 번째 문장에서는 transform만 하면 된다.
x_test = scaler.transform(x_test)

# 모델 생성하기
from sklearn.linear_model import  LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

# 주의 : 상관 분석은 인과 관계가 아니라 연관성과 관련있는 지표이다.
# coef_ 는 w 값을 의미, y 데이터에 대한 x의 인과 관계의 정도를 의미
# 성별과 일등석 탑승 여부가 생사를 판단하는 데 가장 큰 영향력을 미쳤다고 할 수 있다.
print(model.coef_)
print(model.intercept_)

# 샘플 데이터로 예측하기
import numpy as np
a = np.array([0.0, 20.0, 0.0, 0.0])
b = np.array([1.0, 17.0, 1.0, 0.0])
c = np.array([0.0, 32.0, 1.0, 0.0])
d = np.array([0.0, 50.0, 0.0, 1.0])
sample = np.array([a, b, c, d])
print(sample)
sample = scaler.transform(sample)
print(sample)

# 예측하기
pred = model.predict(sample)
print(pred)
print(model.predict_proba(sample)) # proba = probability

# confusion_matrix(정답데이터, 예측데이터)
from sklearn.metrics import confusion_matrix
print('test result')
prediction = model.predict(x_test)
cf_matrix = confusion_matrix(y_test, prediction)
print('confusion matrix')
print(cf_matrix)

# accuracy_score : 정확도를 구해주는 함수
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, prediction)
print(f'accuracy : {accuracy*100:.3f}%')

# 주요 분류와 관련된 metrics(지표)에 대한 보고서
from sklearn.metrics import  classification_report
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
filename = 'titanic01.png'
plt.savefig(filename)
