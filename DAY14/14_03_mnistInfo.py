# 14_03_mnistInfo.py
import numpy as np
'''
손글씨 데이터 셋을 다운로드 하고, 데이터의 구조를 살펴 보도록 한다.
임의의 데이터 하나를 이용하여 시각화 해 본다.
'''
from tensorflow.python.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f'x_train.shape : {x_train.shape}')
print(f'x_train.dtype : {x_train.dtype}')
print(f'x_train.ndim : {x_train.ndim}')
print(f'x_test.shape : {x_test.shape}')
print(f'len(y_test) : {len(y_test)}')
print(f'y_test : {y_test}')

import matplotlib.pyplot as plt
digit = x_train[4] # 숫자 1개 뽑기
plt.imshow(digit)
plt.savefig('mnist_image01.png')
