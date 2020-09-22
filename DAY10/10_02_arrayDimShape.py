# 10_02_arrayDimShape.py
# 배열의 크기(demension)와 형상(shape)
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])
# ndarray : n(정수), d(차원) array(배열 / 행렬)
print(data)
print(type(data))
print(f'rank : {data.ndim}') # 차원
print(f'형상 : {data.shape}')
print(f'몇행 : {data.shape[0]}')
print(f'몇열 : {data.shape[1]}')
print(f'자료형 : {data.dtype}')

# 데이를 가져오는 방법
print(data[0][0], data[1][1], data[1][2]) # data[1][2] : 2열 3행

print(data + data) # 행렬끼리 합치면 행렬의 원소의 합이 리턴

mylist = [1, 2]
print(mylist + mylist) # 리스트끼리 합치면 같은 리스트가 하나 추가

print(data * 10)
print(data * data)
print(1 / data)
print(data ** 0.5)
print(np.sqrt(data))