# 10_01_makeArray.py
# 배열을 생성하는 여러 가지 방법
import numpy as np
print(np.zeros(3))

arr = np.zeros((2, 2)) # 0으로 이루어진 2행 2열 행렬 만들기
print(arr)

arr2 = np.ones((3, 2)) # 1로 이루어진 2행 3열 행렬 만들기
print(arr2)

# 크기가 3인 단위 행렬을 만들어 줍니다.
# 연립 방정식을 풀 때 사용(가우스 소거법)
# 정방 행렬 : 행과 열의 크기가 같은 행렬
arr3 = np.eye(3)
print(arr3)

arr4 = np.full((2, 2), 5) # 5로 이루어진 2 X 2 행렬 생성
print(arr4)