# 12_07_logicalTest03.py
# 엑셀 파일을 읽어 훈련 데이터와 테스트 데이터를 7대 3으로 분리
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.model_selection import train_test_split

filename = 'logicalTest03.csv'
data = np.loadtxt(filename, delimiter=',', dtype=np.int32)

table_col = data.shape[1]
y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column]
y = data[:, x_column:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = Sequential()
model.add(Dense(input_dim=x_column, units=y_column, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x_train, y_train, epochs=5000, batch_size=100, verbose=0)
print(x_test.shape)

total, hit = 0, 0
for i in range(len(x_test)):
    print(y_test[i])
    # pred = np.argmax(model.predict(np.array([i])), axis=-1)
    pred = model.predict_classes(np.array([x_test[i]]))
    print('테스트용 데이터 : %s' % x_test[i])
    print('정답 : %s' % y_test[i], end=' ')
    print('예측 값 : %s' % str(pred.flatten()))

    total += 1

    # 예측 값과 정답이 같은 경우 1추가
    hit += int(y_test[i] == pred.flatten())
    print('-' * 30)
# end for

accuracy = hit / total
print('정확도 = %.4f' % (accuracy))

print('finished')