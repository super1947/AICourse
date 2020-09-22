# 1부터 10까지의 정수 중에서 짝수의 총합과 홀수의 총합을 각각 구해 보세요.

odd = even = 0
for idx in range(1, 11):
  if idx % 2 == 0:
    even += idx
  else:
    odd += idx

print(f'홀수 총합 : {odd}')
print(f'짝수 총합 : {even}')

# 1부터 50까지의 정수 중에서 3의 배수가 아닌 수
# sumA = 1 + 2 + 4 + 5 + 50
# sumB = 3 + 6 + 9 + 48
# sumA - sumB

sumA = sumB = 0
for idx in range(1, 51):
  if idx % 3 == 0:
    sumB += idx
  else:
    sumA += idx
result = sumA - sumB

print(f'결과 : {sumA} - {sumB} = {result}')

