# updownTest.py
# 모듈을 사용하고자 할 때 import 키워드를 사용
import random # random 모듈 : 랜덤한 data를 추출하고자 할 때
# for idx in range(1, 11):
#   answer = random.randint(1, 100)
#   print(answer)

answer = random.randint(1, 100)
count = 0
while True:
  userInput = int(input('숫자를 입력하세요 : '))
  count += 1
  if answer == userInput:
    print(f'정답입니다 : {answer}, {count}번만에 맞췄습니다!')
    break
  elif answer > userInput:
    print(f'UP, 시도 횟수 : {count}')
  else:
    print(f'DOWN, 시도 횟수 : {count}')


