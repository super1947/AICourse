# 14_02_irisSoftMax01.py

from pandas import DataFrame
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd


df = pd.read_csv('newiris.csv')
print(df.columns)
print(df['Species'].unique())

data = df.values
print(data)

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y_temp = data[:, x_column:]
y_temp = y_temp.ravel()  # 1차원 형식으로 만들기

# y_temp를 숫자로 변경
le = LabelEncoder()
le.fit(y_temp)
y = le.transform(y_temp)
print(y)

x = x.astype(np.float)
y = y.astype(np.float)

# 데이터 셋 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)

# 원핫 인코딩
y_train = np_utils.to_categorical(y_train, num_classes=3, dtype='float32')
print(y_train)

# 모델 생성
model = Sequential()
model.add(Dense(units=3, input_dim=x_column, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd', metrics=['accuracy'])
hist = model.fit(x_train, y_train, epochs=1000, batch_size=100, verbose=1)
print(hist.history.items())

total_list = []
for i in range(len(x_test)):
    H = model.predict(np.array([x_test[i]]))
    pred = np.argmax(H, axis=-1)
    print(f'예측값 : {pred}, 정답 : {y_test[i]}')
    print(f'가설정보 : {H.ravel()}')
    total_list.append([float(pred.item()), y_test[i]])

myframe = DataFrame(total_list, columns=['예측값', '정답'])
filename = './irisSoftMaxResult.csv'
myframe.to_csv(filename)
