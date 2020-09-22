# makeIterable01.py
# Iterable : 반복 가능한
# list, tuple, dict, string = iterable object

# list comprehension, set comprehension, dict comprehension
mylist01 = [i for i in range(1, 5)]
print(mylist01)
print('-' * 30)

mylist02 = [2 * i for i in range(1, 5)]
print(mylist02)

# 1, 4, 7, ... 100
mylist03 = [i for i in range(1, 101, 3)]
print(mylist03)
print(sum(mylist03)) # min, max

mylist04 = [i for i in range(1, 101, 3) if i % 10 == 0]
print(mylist04)

# 1부터 10까지 정수 중에서 3의 배수가 아닌 수들의 총합
mylist05 = [i for i in range(1, 101, 3) if i % 3 != 0]
print(mylist05)
print(sum(mylist05))

#중첩 for
mylist06 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(mylist06)
print('-' * 50)

mylist = [('김', 10), ('이', 20), ('최', 30)]
mydict = {data[0]:data[1] for data in mylist}
print(mydict)

student = [('이순신', 80, 90, 10), ('김유신', 70, 40, 20)]

#student를 사용하여 다음과 같은 사전을 만들어 보세요.
# '이순신':(80, 90), '김유신':(70, 40)

studentdict = {data[0:3] for data in student}
print(studentdict)


