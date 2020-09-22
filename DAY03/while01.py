# while01.py
# 1부터 10까지의 총합

total = 0
i = 1
while i < 11:
  total += i
  i += 1
print(f'총합 : {total}')

# 2 + 5 + 8 ... + 50

total = 0
i = 2
while i < 51:
  total += i
  i += 3
print(f'총합 : {total}')

total = 0
i = 1
while i < 100:
  total += i
  i += 2
print(f'총합 : {total}')