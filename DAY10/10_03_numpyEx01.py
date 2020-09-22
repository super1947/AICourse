# 10_03_numpyEx01.py
import numpy as np
data = np.array([[10, 20], [30, 40]])
# print(data)

# sum() : array의 모든 요소의 합을 리턴
result = np.sum(data)
print(result)

# 0 : 행, 1 : 열
result = np.sum(data, axis=0) # 각 행의 값의 합?
print(result)

result = np.sum(data, axis=1) # 각 열의 값의 합을 리턴?
print(result)

result = np.mean(data)
print(result)

result = np.min(data)
print(result)

result = np.max(data)
print(result)

result = np.max(data, axis=0)
print(result)