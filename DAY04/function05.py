# function05.py
# 함수의 마지막에는 return 구문이 들어감.
# 만약 명시하지 않으면 return None 라는 구문이 숨어 있음.
# None : 리턴하지 않는, 의미가 없는, void, vacant, empty, no response

# def namePrint(name, age):
#     print(f'{name}님의 나이는 {age}살입니다.')
#     return None


# name = '제시카'
# age = 20
# result = namePrint(name, age)
# print(result)
# if result == None:
#     print('데이터를 구하지 못했습니다.')
# else:
#     print('참 잘했어요.')

print('-'*50)


def gugudan(num):
    for i in range(1, 10):
        print(f'{num} X {i} = {num * i}')


num = 5
gugudan(num)

# 2, 4, 7단을 출력해 보세요.
mylist = [2, 4, 7]
for i in range(0, len(mylist)):
    gugudan(mylist[i])


def gugu(n):
    newlist = [n * i for i in range(1, 10)]
    return newlist

# su = 3
# print(gugu(su))

# 2단부터 4단까지 각 단의 결과를 list형식으로 출력


def gugu2(a, b):
    for x in range(a, b+1):
        newlist = [x * i for i in range(1, 10)]
        print(newlist)


gugu2(2, 5)
