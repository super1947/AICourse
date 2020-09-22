# function01.py
'''
함수 : 반복적인 행위를 수행하기 위하여 미리 작성해 놓은 소스 코드
매개 변수 : 함수의 소괄호 부분에 입력해주는 값
인자 = 인수 = argument = parameter
함수의 종류 : 내장 함수( abs, pow, sum min 등등)
              사용자 정의 함수
함수를 작성하는 절차
1) 함수 선언
def = define, 함수 이름은 임의로 작성
return 구문은 데이터를 반환할 때 사용, optional
return 구문을 사용하지 않으면 None이 반환
None 키워드는 부정적인 용어인데, void, empty, no 등의 의미로  사용되는 개념
def 함수이름(매개변수1, 매개변수2 ...):
    본문
    [return 반환할 데이터]
2) 함수 호출
'''


# 어떠한 숫자를 입력하면 5를 더해주는 함수 구현

# def addfive(a):
#   return a + 5
#
# print(addfive(5))

def plus5(su):
    return su + 5


su1 = 14
result = plus5(su1)  # 함수를 호출
print(f'결과 01 : {result}')
print(f'결과 02 : {plus5(100)}')

for idx in range(3, 12, 4):
    print(plus5(idx))

mylist = [10, 20, 30]
print('-'*30)
for item in mylist:
    print(plus5(item))
total = 0
for item in mylist:
    total += plus5(item)

print(total)

mytuple = tuple([4, 8, 12])
for item in mytuple:
    print(plus5(item))
