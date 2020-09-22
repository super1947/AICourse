# exception01.py
try:
    x = 4
    y = 0
    mydict = {'a': 10}
    print(mydict['b'])
    mylist = [1, 2, 3]
    print(mylist[4])
    z = x / y
    print(z)
except ZeroDivisionError as err: # 0으로 나눴을 때
    print('0으로 나누시면 안됩니다.')
    print(err)
except IndexError as err: # 인덱스 범위를 초과하여 접근 시도 시 발생
    print('인덱스 범위 관련 오류 발생')
    print(err)
except KeyError as err: # 사전에 해당 키가 존재하지 않을 때
    print('키 관련 오류 발생')
    print(err)
except Exception as err:
    print('기타 나머지 예외 발생')
    print(err)
else:
    print('예외가 없으면 이 라인이 실행됩니다.')
finally:
    print('예외 발생 여부에 관계없이 무조건 실행됩니다.')

'''
예외 처리 : 예외가 사전에 발생하지 않도록 막음 조치를 취하는 것
- except 구문은 1번 이상 사용 가능
예외 처리 방법
try:
    일반적인 코드 작성
except 예외클래스 이름 [ as 예외별칭 ]:
    적당한 오류 메시지 작성
else:
    예외가 없을 때 실행
finally:
    예외와 관계없이 무조건 실행
    ex) 주로 마감 작업(파일 닫기, 데이터베이스 접속 종료)
'''