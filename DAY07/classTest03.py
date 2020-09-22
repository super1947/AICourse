# classTest03.py
'''
계산기 A : 3 + 4 = 7
계산기 B : 5 + 15 = 20
1. 클래스 정의
2. 객체 생성
3. 변수에 값을 할당하거나, 메소드 호출
4. 출력이나 다른 용도로 사용
'''
# 클래스 구성 요소 : 변수, 함수, 생성자(__init__)
# 생성자 : 내부에 들어 있는 변수들의 초기화 용도
# self 키워드 : 호출하고 있는 객체의 정보가 복사되는 변수
class Calculator:
    def __init__(self, data):
        self.result = 0
        self.data = data
        print(f'계산기 생성 완료! 이름 : {self.data}')
        print(f'계산기 초기 값 : {self.result}')

    def calc(self, num):
        self.result += num
        return self.result

# 객체 생성 : 해당 클래스를 이용하여 객체 생성
# Calculator는 생성자
# 규칙 : 생성자의 이름은 클래스의 이름과 동일해야 한다.
calc1 = Calculator('계산기A')
print(calc1.calc(3))
print(calc1.calc(4))

calc2 = Calculator('계산기B')
print(calc2.calc(5))
print(calc2.calc(15))