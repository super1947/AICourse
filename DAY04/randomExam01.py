# randomExam01.py
# 주사위를 10번 던져서 나온 눈의 총합을 구해주는 jusawee 함수를 만들어 보세요.
# 단, 시도 횟수가 입력되지 않으면 5번 던짐
import random
def jusawee(su=5):
  total = 0
  for i in range(su):
    result = random.randint(1, 6)
    total += result
  print(total)



sido = 10 # 시도 횟수
jusawee(sido)

