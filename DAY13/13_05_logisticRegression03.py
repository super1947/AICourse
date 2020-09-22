# 13_05_logisticRegression03.py
import pandas as pd
filename = 'pima-indians-diabetes.csv'
data = pd.read_csv(filename)
print(data.columns)

x_data = data[['pregnant', 'plasma', 'pressure', 'thickness', 'insulin', 'BMI', 'pedigree', 'age']]
y_data = data[['class']]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import  LogisticRegression
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

# 샘플 데이터로 예측하기
import numpy as np
a = np.array([5.0, 180.0, 70.0, 30.0, 0.0, 23.5, 0.153, 40.0])
b = np.array([0.0, 80.0, 80.0, 0.0, 50.0, 26.3, 0.523, 22.0])
c = np.array([10.0, 103.0, 88.0, 40.0, 80.0, 30.1, 0.332, 23.0])
d = np.array([2.0, 150.0, 90.0, 10.0, 100.0, 40.0, 0.215, 52.0])
sample = np.array([a, b, c, d])
print(sample)
sample = scaler.transform(sample)
print(sample)

# 예측하기
pred = model.predict(sample)
print(pred)
print(model.predict_proba(sample)) # proba = probability

# HeatMap 그리기
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
sns.heatmap(pd.DataFrame(cf_matrix), annot=True, cmap='YlGnBu', fmt='g')
plt.title('confusion matrix')
plt.ylabel('actual label')
plt.xlabel('prediction label')
filename = 'pima-indians-diabetes.png'
plt.savefig(filename)
