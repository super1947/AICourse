# 11_03_singleLinear01.py
import numpy as np
# sklearn : science kit(머신 러닝을 하기 위한 패키지)
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
'''
1. 첨부한 엑셀 파일을 읽어 옴
2. 훈련/학습 데이터와 테스트 데이터의 비율을 75대 25로 분리
3. 훈련/학습 데이터를 이용하여 선형 회귀 분석을 한 다음,
4. 테스트 데이터를 이용하여 결과를 예측
'''
filename = 'singleLinear01.csv'
data = np.loadtxt(filename, delimiter=',')
# print(type(data))
# print(data)

table_col = data.shape[1] # 컬럼 수
y_column = 1 # 정답 데이터 컬럼 수
x_column = table_col - y_column # 입력 데이터 컬럼 수

x = data[:, 0:x_column]
y = data[:, x_column:]
# print(x)
# print(y)

'''입력용학습, 입력용 테스트, 출력용 학습, 출력용 테스트
= train_test_split(입력원본, 출력원본, test_size=테스트데이터의 비율)
테스트 비율은 보통 7 : 3으로 많이 나눔'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print(x_train, '#', y_train)

'''
##### keras 사용 순서 #####
1. 모델 생성 model = Sequential()
2. 레이어 추가 model.add() # 총 레이어 수 : add() 함수 개수 + 1       
# Dense() : 레이어를 추가할때 사용하는 클래스 #units=출력값의 크기, #input_dim=입력데이터의 크기, #activation=활성화함수
3. 컴파일 model.compile()
#loss=비용(손실) 함수를 지정, #optimizer=경사하강법을 위한 가이드
4. 학습(훈련) model.fit()
#epoch=반복 횟수, #batch_size=1번에 수행할 데이터의 양 
#verbose=0(진행 결과를 출력하지 않음), 1(실행할 때 마다 출력), 2(epoch당 1번)
# 교사 학습법 : 입력 데이터와 출력(정답) 데이터를 같이 넣어주는 학습법
5. 예측하기 model.predict()
'''
model = Sequential()
model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=5000, batch_size=10, verbose=0)
prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx] # 정답 데이터
    pred = prediction[idx] # 예측치
    print(f'real : {label}, prediction : {pred}')












