
mydict = {'김철수': 35, '박영희': 50, '홍길동': 40}

for key, value in mydict.items():
    print('{}의 나이는 {}살입니다.'.format(key, value))

print('-' * 30)

findkey = '심형래'
if findkey in mydict:
    print(findkey + "은 존재함")
else:
    print(findkey + "은 존재 안 함")

print('-' * 30)

result = mydict.pop('홍길동')
print('pop 이후 내용 : ', mydict)
print(result)  # 40 value만 담김
