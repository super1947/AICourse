# variantArgs02.py
# minval : 튜플 요소에서 가장 큰 수와 가장 작은 수를 반환하는 함수 만들기
def minval(*args):
  return min(args), max(args)
print(minval(3, 5, 8, 2, 4))


# 튜플은 sort() 함수가 불가능. list만 가능
def minval2(*args):
  mylist = [i for i in args]
  mylist.sort()
  return mylist[0], mylist[-1]
print(minval2(3, 5, 8, 2, 4))