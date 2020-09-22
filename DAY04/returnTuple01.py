# returnTuple01.py
# 튜플을 사용하여 반환되는 데이터를 여러 개 만들기
def myfunc(su1, su2):
  if su2 == 0:
    temp = su1
  else:
    temp = su1 // su2
  return su1 + su2, su1 - su2, su1*su2, temp

su1 = 14
su2 = 5
result = myfunc(su1, su2)
print(result)

# 리스트의 모든 요소의 절대값을 구하고, 최대, 최소, 총합, 평균을 튜플로 반환
# 출력 결과 : (50, 10, 150, 30)
mylist = [10, -20, 30, -50, 40]
def myfunc2(data):
  newlist = [abs(i) for i in data]
  mymax = max(newlist)
  mymin = min(newlist)
  mysum = sum(newlist)
  myaverage = mysum // len(newlist)
  return mymax, mymin, mysum, myaverage
result = myfunc2(mylist)
print(type(result), result)