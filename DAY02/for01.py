
# range() 함수 : 반복문에서 특정 횟수만큼 요소들을 반복시킬 때 사용
# range(start, end, step)

for idx in range(1, 11):
    print(idx)

print('-' * 30)

for idx in range(11):
    print(idx)
print('-' * 30)


for idx in range(1, 10, 2):
    print(idx)
print('-' * 30)


for idx in range(10, 1, -1):
    print(idx)

# 1부터 10까지의 총합 구하기

total = 0
for num in range(1, 11):
    total += num

print(f'총합 : {total}')

total2 = 0
for num in range(1, 101, 3):
    total2 += num

print(f'총합 : {total2}')

total3 = 0
for num in range(97, 1, -5):
    total3 += num

print(f'총합 : {total3}')

total4 = 0
for num in range(1, 100, 5):
    total4 += num * num # = num ** 2 = pow(num, 2)
print(f'총합 : {total4}')

# 사용자로부터 숫자를 하나 입력 받고, 1부터 해당 수 까지의 총합 구하기
# 만약 음수를 입력하면 절대값으로 변경하도록 함

userInput = int(input('숫자를 입력하세요 : '))
if userInput < 0:
   userInput = abs(userInput)

total5 = 0
for num in range(1, userInput+1):
    total5 += num
print(f'출력 결과 : 1부터 {userInput} 까지의 합은 {total5}입니다.')

