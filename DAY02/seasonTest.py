month = int(input('달을 입력하세요 : '))

if 9 <= month <= 11:
  print(f'{month}월은 가을입니다')
elif 1 <= month <= 2 or month == 12:
  print(f'{month}월은 겨울입니다')
elif 3 <= month <= 5:
  print(f'{month}월은 봄입니다')
else:
  print(f'{month}월은 여름입니다')