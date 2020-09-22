# myArrSum.py
# 리스트의 모든 요소들의 합을 구해주는 arrsum을 만들어 보세요.

def arrsum(data):
  total = 0
  for i in data: # for문을 이용
    total += i
  return total

def arrsum2(data):  # sum 함수를 이용
  return sum(data)

mylist = [10, 20, 30, 40] # 리스트
print(arrsum(mylist))
print(arrsum2(mylist))

mydata = (1, 2, 3) # 튜플
result = arrsum(mydata)
print(result)

myset = set((1, 2, 3, 4))
result = arrsum(myset)
print(result)