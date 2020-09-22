# starPrint.py
# showStar() 함수를 이용하여 별을 num개 만큼 출력하는 프로그램 작성
# 만약 매개변수를 입력하지 않으면 10개를 출력하도록 합니다.

def showStar(num=10):
    # print('*' * num)
    if num < 0:
        num = abs(num)
    for i in range(num):
        print('*', end='')


showStar(5)
showStar()

# for i in range(1, 11):
#     showStar(i)

# showStar(-7)

# for item in [3, 5]:
#     showStar(item)
