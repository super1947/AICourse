# defaultArgs01.py
# 매개 변수가 2개이고, 둘 다 필수 사항이다.
def func01(a, b):
    return 2 * a + b
# print(func01())
# # TypeError: func01() missing 2 required positional arguments: 'a' and 'b' -> 필수 매개 변수 2개가 누락
# print(func01(3, 5, 3))
# TypeError: func01() takes 2 positional arguments but 3 were given -> 매개 변수 개수 초과

# 옵션 매개 변수(필수 사항 아님) a=2, b=1은 default value,
# 매개변수 자리에 다른 인수를 넣으면 인수로 대체
def func02(a=2, b=1):
    return 2 * a + b

# positional arguments (위치 기반 매개 변수)
print(func02())
print(func02(3))
print(func02(3, 5))

#keyword arguments (키워드 기반 매개 변수)
print(func02(b=2, a=1))
print(func02(2, b=1))
# print(func02(b=1, 2)) -> SyntaxError: positional argument follows keyword argument