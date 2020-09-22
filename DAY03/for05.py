# for05.py
mystring = input('문자열 입력 : ') # python is very easy
mylist = mystring.split()
print(type(mylist)) # type 함수는 해당 데이터의 유형을 알려주는 함수
print(mylist)

for i in range(len(mylist)):
  if i % 2 == 0:
    mylist[i] = mylist[i].upper()
  else:
    mylist[i] = mylist[i].lower()
print(mylist)
result = '#'.join(mylist)
print(result)