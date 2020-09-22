# juminNumber.py
# 주민번호는 반드시 14자리여야 한다.
# 6번째 항목은 반드시 '-'
# 2번째 항목은 '0'또는 '1'
# 7번째 항목은 '1 ~ 4'


def findSsn(juminNum):
  if len(juminNum) != 14:
    return False
  if juminNum[6] != '-':
    return False
  if not juminNum[2] in  ['0', '1']:
    return False
  if not juminNum[7] in ['1', '2', '3', '4']:
    return False
  # print(juminNum[0:6].isdigit())
  # print(juminNum[7:].isdigit())
  if not (juminNum[0:6].isdigit()) or not (juminNum[7:].isdigit()):
    return False
  return True
# 문자열.isdigit() 함수를 이용하면 숫자들로 구성되었는지 확인 가능
juminList = ['701226-1710566', '7012261710566', '703226-1710566', '701226-5710566', '8103가나-1234567', '911211-1나다라마바사']

for juminNum in juminList:
  result = findSsn(juminNum)
  if result == True:
    print(f'{juminNum}는 올바른 주민번호 입니다.')
  else:
    print(f'{juminNum}는 잘못된 주민번호 입니다.')
