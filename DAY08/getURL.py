# getURL.py
# 네이버 사이트의 url 정보 취득
import urllib.request
url = 'http://www.naver.com'

# parameter 추가
# ?는 url과 parameter의 구분자 역할
# =는 파라미터 이름과 실제 값의 구분자 역할
# &는 파라미터 간의 구분자 역할
parameter = '?'
parameter += 'id=asdf'
parameter += '&password=1234'
parameter += 'message=hahaha'
# req : 요청 객체
req = urllib.request.Request(url)
# response : 응답 객체
response = urllib.request.urlopen(req)
print(response)
# 응답 객체를 바이트 형태로 바꾼 다음 텍스트로 변환
print(response.read().decode('utf-8'))
