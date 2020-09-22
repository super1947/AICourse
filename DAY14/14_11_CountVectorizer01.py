# 14_11_CountVectorizer01.py
from sklearn.feature_extraction.text import CountVectorizer
'''
CountVectorizer : 문자열에서 단어 토큰을 생성하여 BOW로 인코딩된 벡터를 생성

'''
sentences = ['우리 아버지 고향 친구 이름은 손흥민 손흥민', '손흥민 고향 친구 이름은 박지성 박지성', '고향 친구 있나요.']
# min_df = minimum document frequency
#  !주의 : min_df 쓸 때 한 문장에 2번 나오면 하나로 취급한다.
#          최소 빈도가 2번 이상인 단어들만 뽑아달라.
# stop_words : 불용어
vectorizer = CountVectorizer(min_df=2, stop_words=['친구'])
# 단어 사전
mat = vectorizer.fit(sentences)
print(type(vectorizer))
print(type(mat))
print(mat.vocabulary_)
print(sorted(mat.vocabulary_.items()))
# 토큰
features = vectorizer.get_feature_names()
print(features)
print(type(features))
print(vectorizer.get_stop_words())

myword = [sentences[0]]
print(myword)
myarray = vectorizer.transform(myword).toarray()
print(type(myarray))
print(myarray)

'''
0이 1번, 1이 0번, 2가 2번, 3이 1번 ...
myarray = [[1 0 2 1 1 1 0]]
mat = {'우리': 4, '아버지': 3, '고향': 0, '이름은': 5, '손흥민': 2, '박지성': 1, '있나요': 6}
myword = ['고향', '박지성', '손흥민', '아버지', '우리', '이름은', '있나요']
'''
