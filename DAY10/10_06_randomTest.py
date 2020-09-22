# 10_06_randomTest.py
import numpy as np
print('임의의 값으로 채워진 행렬 생성')
result = np.random.random((2, 2))
print(result)

print('표준 편차가 1, 평균이 0인 정규 분포에서 표본 추출')
result = np.random.randn(2, 3)
print(result)

print('임의의 값으로 채워진 배열 생성')
result = np.random.rand(4, 4)
print(result)

print('균등 분포에서 데이터 추출')
result = np.random.uniform(size=(3, 3))
print(result)

print('정수 0 이상 5미만의 정수 추출')
result = np.random.randint(3, size=4)
print(result)
result = np.random.randint(0, 5, size=(10, 10))
print(result)

# 0, 1, 2 중에서 임의로 하나를 추출하는 동작을 5번 수행하여
# 나온 수의 총합

result = np.random.randint(0, 3, size=5)
print(result)
total = np.sum(result)
print(total)

# 시드 배정은 동일한 데이터를 샘플링하거나
# 머신 러닝 시 동일한 결과를 한시적으로 추출해보고자 할 때 사용
# seed = 12345
# np.random.seed(seed) # 랜덤 값에 시드 배정
length = 10
result = np.random.permutation(length) # 0부터 length 까지의 수를 무작위로 섞어 하나씩 반환
print(result)

# 0부터 4미만 임의의 수 3개 추출
result = np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
print(result)                    #  0   1   2    3   4  (0 : 10%, 1:0%, 2:30%, 3:60%, 4:0%)