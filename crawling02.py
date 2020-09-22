# crawling02.py
# 수집할 내용 :
import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

tags = soup.findAll('div', attrs={'class':'tit3'})
print(tags)
for tag in tags:
    print(tag.a.string)

print('<a> 태그의 href 전체 태그')
url_header = 'https://movie.naver.com'
for tag in tags:
    print(url_header + tag.a['href'])

mytrs = soup.find_all('tr')
print(len(mytrs))

no = 0
totallist = []
for one_tr in mytrs:
    # print(one_tr)
    # print('@'*30)
    title = ''
    up_down = ''
    mytd = one_tr.find('td', attrs={'class':'title'})
    # print(mytd)
    if(mytd != None):
        no += 1
        newno = str(no).zfill(2)
        mytag = mytd.find('div', attrs={'class':'tit3'})
        title = mytag.a.string # string 속성 : 해당 태그가 가지고 있는 문자열을 출력
        mytd = one_tr.select_one('td:nth-of-type(3)') # td 태그 중에서 3번째 요소 찾기
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up':
            up_down = '상승'
        elif myimg.attrs['alt'] == 'down':
            up_down = '강등'
        else:
            up_down = '불변'
        change = one_tr.find('td', attrs={'class':'range ac'})
        change = change.string
        totallist.append((newno, title, up_down, change))
        print(totallist)
mycolumn = ['순위', '제목', '변동', '변동폭']
myframe = DataFrame(totallist, columns=mycolumn)
filename = 'naverMovie.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)

print(filename + '파일 저장됨')