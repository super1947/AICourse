# naverCartoon.py
from bs4 import BeautifulSoup
# urlopen : 네트워크에 존재하는 주소를 열어주는 함수
from urllib.request import urlopen
from pandas import DataFrame
import os, shutil # shutil : shell utility
myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
print(type(soup))

# 요일별 폴더 생성
weekday_dict = {'mon':'월요일', 'tue':'화요krk일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일', }

myfolder = 'd:\\imsi\\'
try:
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)
    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        if os.path.exists(mypath):
            shutil.rmtree(mypath) # rmtree : remove tree
        os.mkdir(mypath)

except FileExistsError as err:
    print(err)

# 각 이미지를 저장해주는 함수
def saveFile(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc)
    filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
    myfile = open(filename, mode='wb')
    myfile.write(image_file.read()) # 바이트 형태로 저장
    myfile.close()


mytarget = soup.find_all('div', attrs={'class': 'thumb'})
mylist = [] # 데이터를 저장할 리스트
for x in mytarget:
    myhref = x.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]

    imgtag = x.find('img')
    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?','').replace(':','')
    mysrc = imgtag.attrs['src']
    saveFile(mysrc, myweekday, mytitle)

    sublist = [mytitleid, myweekday, mytitle, mysrc]
    # sublist.append(mytitleid)
    # sublist.append(myweekday)
    # sublist.append(mytitle)
    # sublist.append(mysrc)
    mylist.append(sublist)

mycolumns = ['타이틀번호', '요일', '제목', '소스']
myframe = DataFrame(mylist, columns=mycolumns)
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding='utf-8', index=False) # index = 행 번호
