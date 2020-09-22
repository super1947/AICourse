# 12_09_surgeryTest.py
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.model_selection import train_test_split

filename = 'surgeryTest.csv'
data = np.loadtxt(filename, delimiter=',', dtype=np.int32)

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = Sequential()
model.add(Dense(input_dim=x_column, units=512, activation='relu'))
model.add(Dense(units=y_column, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3000, batch_size=100, verbose=0)
# 모델 관련 속성
print(model.inputs) # input tensor information
print('-'*50)
print(model.outputs) # output tensor information
print('-'*50)
print(model.layers) # add() 함수를 사용한 레이어들의 주소 정보
print('-'*50)
# metrics : 성능 지표 , 기본값으로 cost func를 항상 표시
# 추가하려면 compile 함수의 metrics=[]형식으로 넣어주면 된다.
print(model.metrics_names)
pred = model.predict_classes(x_test)
for i in range(len(pred)):
    label = y_test[i]
    print(f'real : {float(label):.3f}, pred : {float(pred[i]):.3f}')