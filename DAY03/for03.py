examdata = [90, 30, 65, 45, 80]
print(examdata)

for item in examdata:
  print(item)
print('-'*30)

# 점수가 60 이상이면 합격, 그렇지 않으면 불합격으로 처리하기
for idx in range(len(examdata)):
  print(examdata[idx])
print('-' * 30)

for idx in range(len(examdata)):
  if examdata[idx] >= 60:
    print(f'{idx + 1}번째 응시자 {examdata[idx]} : 합격')
  else:
    print(f'{idx + 1}번째 응시자 {examdata[idx]} : 불합격')
print('-' * 30)

# continue 구문 : 반복문을 실행하다가 continue를 만나면 이후 구문은 실행이 안되고,
# 다음 step으로 넘어감.
print('합격자만 출력하기')
for idx in range(len(examdata)):
  if examdata[idx] >= 60:
    print(f'{idx + 1}번째 응시자 {examdata[idx]} : 합격')
  else:
    continue
print('-' * 30)

