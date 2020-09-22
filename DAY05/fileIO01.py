# fileIO01.py
# 파일 입출력
# open() : 텍스트/바이너리 파일을 읽거나 쓰기 위한 함수
# myfile01 = open(file='전체경로+파일이름', mode='', encoding='utf-8')
# mode : *r(read)/ w(write) / a(append)       ||        *t(text)/b(binary)   *기본값
# encoding : 인코딩 문자열('utf-8' , 'utf-16')
myfile01 = open(file='newfile.txt', mode='wt', encoding='utf-8')
for i in range(1, 11):
    # 문자열 '\n'은 엔터키를 의미합니다.
    data = f'{i}번째 줄입니다.\n'
    myfile01.write(data)
myfile01.close()

myfile02 = open(file='newfile.txt', mode='a', encoding='utf-8')
for i in range(11, 101):
    data = f'{i}번째 줄입니다.\n'
    myfile02.write(data)
myfile02.close()

print('여러 개 파일 만들기')
for i in range(1, 11):
    filename = 'somefile' + str(i).zfill(2) + '.txt'
    myfile = open(filename, 'w', encoding='utf-8')
    data = f'메롱 {str(i).zfill(5)}'
    myfile.write(data)
    myfile.close()

# with 구문은 암시적으로 close를 수행해 줍니다.
# 따라서 close() 함수를 사용하지 않아도 됩니다.
print('with 구문 사용하기')
with open(file='test.txt', mode='w', encoding='utf-8') as myfile:
    myfile.write('메롱\n')
    myfile.write('하하\n')
    print('가나다라', file=myfile)

with open(file='test.txt', mode='r', encoding='utf-8') as myfile:
    print(myfile.read())
    print(type(myfile.read()))
    print(myfile.readlines())

print('finished')