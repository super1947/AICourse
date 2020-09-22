# 14_12_TfIdfVectorizer01.py
# Tfidf = TF * IDF
# 모든 문서에 공통적으로 들어있는 단어는 변별력이 떨어짐. (가중치가 적다.)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1, stop_words=['친구'])
sentences = ['우리 아버지 여자 친구 이름은 홍길동 홍길동', '홍길동 여자 친구 이름은 심순애 심순애', '여자 친구 있나요.']
mat = vectorizer.fit(sentences)
print('단어 사전')
print(mat.vocabulary_)
print(vectorizer.get_feature_names())
print(vectorizer.get_stop_words())
myword = [sentences[2]]
print(myword)
myarray = vectorizer.transform(myword).toarray()
print(myarray)

ft = vectorizer.fit_transform(sentences).todense()
print(ft)