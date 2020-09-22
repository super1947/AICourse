# 12_02_linearRegression01.py
# sklearn을 이용한 회귀 분석
# 결정 계수 : 실제 값과 예측 값이 얼마 정도의 일치성을 보이는지 나타내는 척도
#             값은 0 ~ 1, 1에 가까우면 설명력이 좋다고 표현
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 학습용 데이터 셋 : 'linearTest01.csv'
# 테스트용 데이터 셋 : 'linearTest02.csv'
filename = 'linearTest01.csv'
training = np.loadtxt(filename, delimiter=',', skiprows=1) # skiprow=1 : 1열은 데이터에서 제외
print(training)

x_column = training.shape[1] - 1

x_train = training[:, 0:x_column]
y_train = training[:, x_column:]

model = LinearRegression()
model.fit(x_train, y_train) # 학습

print(f'기울기(w) : {model.coef_}')
print(f'절편(w) : {model.intercept_}')
print(f'잔차의 제곱 합(cost) : {model._residues}')

# 시각화
plt.title('키와 몸무게의 상관 관계')
plt.xlabel('키')
plt.ylabel('몸무게')
plt.plot(x_train, y_train, 'bo')

train_pred = model.predict(x_train)
plt.plot(x_train, train_pred, 'r')
filename = 'linearRegression01.png'
plt.savefig(filename)


filename = 'linearTest02.csv'
testing = np.loadtxt(filename, delimiter=',', skiprows=1) # skiprow=1 : 1열은 데이터에서 제외
print(testing)

x_column = testing.shape[1] - 1

x_test = testing[:, 0:x_column]
y_test = testing[:, x_column:]
print(x_test)
print(y_test)

# 산술 연산에 의한 결정 계수 구하기
y_test_mean = np.mean(np.ravel(y_test)) #np.ravel : 2차원을 1차원으로 만들어 주는 함수

# TSS ) 편차 제곱의 총합
TSS = np.sum((np.ravel(y_test) - y_test_mean)**2)

# RSS ) 회귀식과 평균 값의 차이의 총합
RSS = np.sum((np.ravel(y_test) - np.ravel(model.predict(x_test)))**2)

# 결정 계수 = 1 - RSS / TSS
R_Squared = 1 - (RSS / TSS)
print(f'결정계수01 : {R_Squared}')
print(f'결정계수02 : {model.score(x_test, y_test)}')


