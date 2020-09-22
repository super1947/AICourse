# 12_05_logicalTest01.py
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'logicalTest01.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x_train = data[:, 0:x_column]
y_train = data[:, x_column:]

x_test = [[5], [11]]
model = Sequential()
'''
퍼셉트론(perceptron) : ex) 전구 on / off ( 0, 1)처럼 0과 1의 값을 가지고 있는 신경망
perceptron이 linear, logistic, another machine learning으로 바뀌기 위해서는 함수를 지정해줘야 한다
이 때 사용되는 함수를 activation function이라고 한다.
linear = 'linear', logistic = 'sigmoid' 
'''
model.add(Dense(input_dim=x_column, units=y_column, activation='sigmoid'))

# 비용 함수는 이진 분류 이므로 'binary_crossentropy'
# optimizer 사용 시 지정 문자열을 사용해도 되지만, 객체 생성을 통해 만들 수 있습니다.
learning_rate = 0.01 # 학습률
import tensorflow
sgd = tensorflow.keras.optimizers.SGD(lr=learning_rate)
model.compile(loss='binary_crossentropy', optimizer=sgd)
model.fit(x_train, y_train, epochs=5000, batch_size=100, verbose=0)
# 해당 모델에 훈련용 데이터를 이용하여 확률 값을 예측
H2 = model.predict(x_train)
# print(H2)
for i in x_test:
    # predict_classes : 정답이 가지고 있는 클래스의 값을 출력해 줌.
    pred = np.argmax(model.predict_classes(np.array([i])))
    print(f'test data : {np.array([i])}')
    print(pred)
    H = model.predict(np.array([i]))
    # print(H)
