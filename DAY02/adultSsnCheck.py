name = '김철수'
ssn = '122225-3456789'

# 슬라이싱과 if 구문 등을 이용하여 다음과 같이 출력해 보세요.
# 19세 이상이면 성년

'''
출력 결과
이름 : 김철수
주민번호 : 122225-3456789
성별 : 남자
나이 : 8세
체크 : 미성년자 
'''


def gender():
  if ssn[7] == '1' or '3':
    return '남자'
  else:
    return '여자'


def age():
  return (20 - int(ssn[0:2]))


def checkAge():
  now_year = 20
  if now_year - int(ssn[0:2]) >= 19:
    return '성인'
  else:
    return '미성년자'


print(f'이름 : {name}')
print(f'주민번호 : {ssn}')
print(f'성별 : {gender()}')
print(f'나이 : {age()}세')
print(f'체크 : {checkAge()}')

dpos1 = ssn[7]
if dpos1 in ['1', '3']:
  gender = '남자'
else:
  gender = '여자'

apos2 = int(ssn[0:2])  # 출생년도 2자리 수

# birth_year : 출생 년도
if dpos1 in ['1', '2']:
  birth_year = 1900 + apos2
else:
  birth_year = 2000 + apos2

now = 2020
age = now - birth_year

if age >= 19:
  remark = '성인'
else:
  remark = '미성년자'
print('-' * 30)

print(f'이름 : {name}')
print(f'주민번호 : {ssn}')
print(f'성별 : {gender}')
print(f'나이 : {age}세')
print(f'체크 : {remark}')
