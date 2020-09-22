# jsonTest01.py
import json
data = {'age': 30, 'name': '홍길동', 'address': '강남구 역삼동', 'broadcast': {'sbs': 5, 'mbc': 11, 'kbs': 9}}
json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True) # sort_keys : 키를 알파벳 순서대로 정렬
# dumps() : 데이터를 읽어서 str 형태로 바꿔주는 함수
print(json_str)
print(type(json_str))

json_data = json.loads(json_str)
print(json_data)
print(type(json_data))

print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['sbs'])
print(json_data['broadcast']['mbc'])