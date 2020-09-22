# 14_09_mnistResult.py
test_acc = [0.9225, 0.9224, 0.9779, 0.9872, 0.9779]
test_loss = [0.2809, 0.2788, 0.0807, 0.0983, 0.0843]
comment = [f'테스트{i}' for i in range(1, 6)]
print(comment)
mycolor = ['b', 'g', 'r', 'c', 'lime']

import matplotlib.pyplot as plt

# 정확도 그래프
plt.figure()
plt.rc('font', family='Malgun Gothic')
plt.title('테스트 케이스별 정확도')
plt.xlabel('테스트 케이스')
plt.ylabel('정확도')
plt.bar(comment, test_acc, color=mycolor)
filename = 'mnist accuracy graph.png'
plt.savefig(filename)

# 손실함수 그래프
plt.figure()
plt.title('테스트 케이스별 비용 함수')
plt.xlabel('테스트 케이스')
plt.ylabel('비용')
plt.bar(comment, test_loss, color=mycolor)
filename = 'mnist loss graph.png'
plt.savefig(filename)