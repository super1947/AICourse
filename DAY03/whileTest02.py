# whileTest02.py
# 무한 whileLoop : 반복 횟수가 몇 번인지 모를 경우
# 어느 조건을 충족하면 break 구문을 사용하여 종료해야 함.
# cnt = 0
# while True:
#   print('a' + str(cnt))
#   cnt += 1
#   if cnt == 5:
#     break

# 사용자가 입력한 시험 점수에 대한 평균과 개수를 구해 봅시다.
# 음수 값이 입력되면 프로그램을 종료하도록 합니다.


total = 0
count = 0
average = 0.0

while True:
  userInput = int(input('시험 점수를 입력 하세요 : '))
  if userInput <= 0:
    break
  total += userInput
  count += 1
  average = total / count

print(f'총 시험 횟수 : {count}, 총점 : {total}, 평균 : {average:.3f}')