# whileTest01.py
# 숫자 5를 입력 받고 5단 출력하기
# 5 * 1 = 5, 5 * 2 = 10 ...

userInput = int(input('몇 단 출력? : '))

if userInput < 0:
  userInput = abs(userInput)

total = 0
i = 1

while i < 10:
  userInput * i
  print(f'{userInput} * {i} = {userInput * i}')
  i += 1


