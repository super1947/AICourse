# 14_01_softMaxEx01.py

import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'softMaxEx01.csv'
data = np.loadtxt(filename, delimiter=',', encoding='utf-8')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

# 정답이 가질 수 있는 클래스 개수
NB_CLASSES = 3

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
print(y_train)  # 원핫 인코딩 적용 전

# np_utils : 원핫 인코딩 수행
y_train = np_utils.to_categorical(
    y_train, num_classes=NB_CLASSES, dtype='float32')
print(y_train)


model = Sequential()
model.add(Dense(input_shape=(x_column, ), units=3, activation='softmax'))
# 모델의 간략한 정보를 출력해준다.
model.summary()
# 'sgd' : 확률적 경사 하강법
model.compile(loss='categorical_crossentropy',
              optimizer='sgd', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=1000, verbose=0)
print(history)

for i in range(len(x_test)):
    H = model.predict(np.array([x_test[i]]))
    pred = np.argmax(H, axis=-1)
    print(f'예측값 : {pred}, 정답 : {y_test[i]}')
    print(f'가설정보 : {H.flatten()}')
