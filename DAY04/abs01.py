# abs01.py
# 어떠한 숫자에 대해 절대 값으로 만들어 주는 함수 만들기
# 매개 변수 이름은 임의의 이름이어도 된다.

def absolute(n):
  if n < 0:
    n = -n
  return n


su = -5
result = absolute(su)
print(result)
mylist = [2, -4, -7]
newlist = []
for i in mylist:
  newlist.append(absolute(i))
print(newlist) # for 문을 통해 새로운 리스트 만들기
newlist2 = [absolute(i) for i in mylist] # list comprehension 방식으로 리스트 만들기
print(newlist2)
print('finished')



