# bs4Exam02.py
# BeautifulSoup 패키지 : html 문서에서 데이터를 추출하고자 할 때 사용하는 패키지
from bs4 import BeautifulSoup
html = open('fruits.html', 'r', encoding='utf-8') # fruits.html
# parser : html 문서가 제대로 되어 있는지 검증하는 객체
# soup : BeautifulSoup(해당문서, '파싱문자열')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

body = soup.select_one('body')
ptag = body.find('p')
print(ptag['class'])
print(ptag['align'])

# print(ptag['id'])
ptag['id'] = 'apple'
print(ptag['id'])
print(ptag)

body_tag = soup.find('body')
print(body_tag)
# print(body_tag.children)
i = 0
for child in body_tag.children:
    i += 1
    print(f'{i}번째 요소 : {child}')
    print('#'*30)

mydiv = soup.find('div')
print(mydiv)
print(f'my parent : {mydiv.parent}')

# attrs(attribute) : 속성을 이용하여 찾을 때
mytag = soup.find('p', attrs={'class':'hard'})
print('%'*30)
print(mytag)
print(mytag.find_parent())

print('mytag 태그의 모든 상위 부모 태그들의 이름')
parents = mytag.find_parents()
for p in parents:
    print(p.name)
