# rangeSum.py
# 정수 2개를 입력 받아서, 앞 수에서 뒤 수 사이에 있는 모든 정수의 합을 구하세요.

firstnum = int(input('숫자를 입력하세요 : '))
secondnum = int(input('숫자를 입력하세요 : '))

total = 0
if firstnum > secondnum:
  firstnum, secondnum = secondnum, firstnum # swap


for i in range(firstnum, secondnum + 1):
  total += i

total = 0
if firstnum < secondnum:
  for i in range(firstnum, secondnum + 1):
    total += i
else:
  for i in range(secondnum, firstnum + 1):
    total += i

print(f'{firstnum}부터 {secondnum}까지의 총합 : {total}')