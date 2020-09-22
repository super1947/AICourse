# corrTest03.py
# 상관 관계 분석
# numpy : numerical python
# 배열이나 행렬을 이용하여 수치 해석, 머신 러닝 등에 사용되는 모듈
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

def correlation(x, y): # 상관 계수를 구해주는 함수
    x_mean = x.mean()
    y_mean = y.mean()


    numerator = np.sum((x-x_mean)*(y-y_mean))
    print(f'분자 : {numerator}')
    left = np.sqrt(np.sum((x - x_mean) ** 2))
    right = np.sqrt(np.sum((y - y_mean) ** 2))
    denominator = left * right
    print(f'분모 : {denominator}')
    return numerator / denominator

x = np.array([3, 5, 8, 11, 13])
y = np.array([1, 2, 3, 4, 5])

print(correlation(x, y))

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# mymean = y.mean()
# print(mymean)
# mysum = np.sum(y)
# print(mysum)
