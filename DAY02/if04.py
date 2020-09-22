# 다중 택일 구문

name = '김철수'
score = int(input('숫자를 입력하세요'))

grade = ''  # 학점

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'이름 : {name}')
print(f'점수 : {score}')
print(f'학점 : {grade}')
