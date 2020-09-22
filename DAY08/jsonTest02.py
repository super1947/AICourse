#  jsonTest02.py
import json
filename = 'some.json'
myfile = open(filename, mode='rt', encoding='utf-8').read()
print(type(myfile))
json_data = json.loads(myfile)
name = json_data['member']['name']
address = json_data['member']['address']
phone = json_data['member']['phone']
cafename = json_data['web']['cafename']
id = json_data['web']['id']

print(f'이름 : {name}')
print(f'주소 : {address}')
print(f'핸드폰번호 : {phone}')
print(f'카페이름 : {cafename}')
print(f'아이디 : {id}')