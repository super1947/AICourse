# word2vecTest.py
# 문재인 대통령 신년사.txt
from bs4 import BeautifulSoup
from konlpy.tag import Okt

filename = '문재인대통령신년사.txt'
myfile = open(filename, mode='rt', encoding='utf-8')
soup = BeautifulSoup(myfile, 'html.parser')
mytext = soup.text


result = []
okt = Okt()

textlines = mytext.split('\n')
# print(textlines)

for textline in textlines:
    pos = okt.pos(textline, norm=True, stem=True)
    # print(pos)
    temp = []
    for word in pos:
        if not word[1] in ['Josa', 'Eomi', 'Punctuation', 'Verb'] and len(word[0]) >= 2:
            temp.append(word[0])
    # print(temp)
    temp2 = ' '.join(temp).strip()
    # print(temp2)
    result.append(temp2)
# print(result)

prepro_file = 'word2vec.prepro'
with open(prepro_file, mode='wt', encoding='utf-8') as resultfile:
    resultfile.write('\n'.join(result))

# vec : 벡터 - (방향, 크기를 가지고 있는 단위)
# scala : 값만 가지고 있는 단위
# 단어들의 유사도 : cos 유사도, 유클리디언 유사도, 맨해튼 유사도

from gensim.models import word2vec
# LineSentence : 분석을 하기 위한 sentence를 만들어 주는 함수
data = word2vec.LineSentence(prepro_file)
print(type(data))
# word2vec : word to vector 알고리즘
# Word2Vec() : LineSentence로 만든 문장에 대한 모델을 생성
# size : 벡터의 차원수, window : 윈도우 사이즈
# min_count : 빈도수 체크 시 최소 횟수
# sg : 1(skipgram), 0(cbow)
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
model_filename = 'word2vec.model'
model.save(model_filename) # 모델 파일 저장

