# 12_06_logicalTest02.py
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'logicalTest02.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x_train = data[:, 0:x_column]
y_train = data[:, x_column:]

model = Sequential()
model.add(Dense(input_dim=x_column, units=y_column, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x_train, y_train, epochs=5000, batch_size=100, verbose=0)
x_test = [[2, 1], [6, 5], [11, 6]]

# 0 : 강아지, 1 : 고양이
def getCategory(mydata):
    mylist = ['강아지', '고양이']
    print(f'예측 : {mydata}, {mylist[mydata[0]]}')

for i in x_test:
    # pred = np.argmax(model.predict(np.array([i])), axis=-1)
    pred = model.predict_classes(np.array([i]))
    getCategory(pred.flatten()) # flatten() : 다차원을 1차원으로 만들어 주는 함수
    H = model.predict(np.array([i]))
    print(H)

