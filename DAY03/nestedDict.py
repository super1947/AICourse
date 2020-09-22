# nestedDict.py
mylist = [('sale 무료 배송 할인', '스팸'), ('일정 변경', '일반'), ('sale 변경', '일반')]

words = set()  # 단어들을 저장할 집합
word_dict = {} # 카테고리별 각 단어들의 빈도수를 저장할 중첩 사전
category_dict = {} # 카테고리별 빈도수를 저장할 사전

for email, category in mylist:
  if category in category_dict:
    category_dict[category] += 1
  else:
    category_dict[category] = 1

  # 단어별 분리
  result = email.split(' ')
  for one in result:
    words.add(one)

  if not category in word_dict:
    word_dict[category] = {}
  for one in result:
    if one in word_dict[category]:
      word_dict[category][one] += 1
    else:
      word_dict[category][one] = 1

print(f'words 집합 : {words}')
print(f'카테고리 사전 : {category_dict}')
print(f'워드 사전 : {word_dict}')
