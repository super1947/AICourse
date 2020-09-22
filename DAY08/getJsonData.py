# getJsonData.py
import json


def get_Json_Data():
    print('함수 호출됨')
    filename = 'jumsu.json'
    myfile = open(filename, mode='rt', encoding='utf=8').read()
    print(type(myfile))
    jsonData = json.loads(myfile) # loads(str) 문자열 형식의 데이터를 json 타입으로 변환
    for item in jsonData:
        # print(item.keys())
        # print(item.values())
        # print(item.items())
        kor = float(item['kor'])
        eng = float(item['eng'])
        math = float(item['math'])
        total = kor + eng + math
        name = item['name']
        print(f'이름 : {name}')
        print(f'총점 : {total}')

        if 'hello' in item.keys():
            message = item['hello']
            print(f'메세지: {message}')

        _gender = item['gender'].upper()

        if _gender == 'M':
            gender = '남자'
            print(f'성별 : {gender}')
        elif _gender == 'F':
            gender = '여자'
            print(f'성별 : {gender}')
        else:
            gender = '미상'
            print(f'성별 : {gender}')
        print('-' * 30)



if __name__ == '__main__':
    print('나 스스로 실행되었습니다.')
    get_Json_Data()
else:
    print('다른 프로그램이 호출했습니다.')