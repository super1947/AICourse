# xmlEx03.py
from xml.etree.ElementTree import parse

tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
# print(type(myroot))


# print(myroot.keys()) # 해당 속성들의 키를 list 형식으로 반환
# print('-'*50)
# print(myroot.items()) # 해당 속성들의 키와 값을 튜플로 가지는 list를 반환
# print('-'*50)
# print(myroot.get('설명')) # 설명이라는 속성의 값을 반환
# print('-'*50)
# print(myroot.get('qwert', '없을 경우 기본 값')) # 'qwert'라는 속성이 없을 경우 다음 인자를 반환
# print('-'*50)
# print(myroot.find('가족'))
# print('-'*50)
# family = myroot.find('가족')
# childs = list(family)
# for person in childs:
#     # print(person)
#     elem = list(person)
#     # print(elem)
#     for abc in elem:
#         print(abc.text)
#         if abc.text == '이순자':
#             print(abc.attrib['정보'])

allfamily = myroot.findall('가족')
for onefamily in allfamily:
    for person in onefamily:
        name = person.find('이름')
        if name != None:
            print(name.text)
        else:
            print(person.attrib['이름'])
