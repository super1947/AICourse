# 10_04_numpyEx02.py
# 1차원 배열을 형상 변경, 행렬 연산, 전치

import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([3, 6, 1, 2])
print(a.ndim)
print(a.shape)

A = np.reshape(a, [2, 2])
print(A)
print(A.ndim)
print(A.shape)

B = np.reshape(b, [2, 2])
print(B)
print(B.ndim)
print(B.shape)

# matmul : MATrix MULtiply
result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)
print(result3_1)
print(result3_2)

a_14 = np.reshape(a, [1, 4])
b_14 = np.reshape(b, [1, 4])
b2 = np.transpose(b_14) # 행렬 전치 : 1 X 4 행렬을 4 X 1 행렬로 변경

print(a_14)
# print(b_14)
print(b2)

result3_3 = np.matmul(a_14, b2)
print(result3_3)
