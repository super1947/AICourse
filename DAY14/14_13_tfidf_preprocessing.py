# tfidf_preprocessing.py
import pandas as pd

train_data = pd.read_csv('./data_in/train_clean.csv')
print(train_data.info())
print(train_data.columns)
print(train_data['sentiment'].unique())

myseries = train_data.groupby('sentiment')['sentiment']
result = myseries.count()
print(result)

# 리뷰와 정답 데이터를 리스트화
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

from sklearn.feature_extraction.text import TfidfVectorizer
# analyzer : word(단어 단위), char(한 글자 씩)
# max_features : 최대 길이
# ngram_range=(1, 3) : 1, 2, 3개의 단어 ex) very good 을 다 처리한다?
vectorizer = TfidfVectorizer(min_df=0, analyzer='char', max_features=5000, \
                             ngram_range=(1, 3))

import numpy as np
x = vectorizer.fit_transform(reviews)
y = np.array(sentiments)
# print(x)

features = vectorizer.get_feature_names()
print(f'토큰 갯수 : {len(features)}')
print(f'토큰화된 단어 리스트 : {features}')

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)

from sklearn.linear_model import  LogisticRegression
model = LogisticRegression(class_weight='balanced')
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(f'정확도 : {model.score(x_test, y_test):.3f}')

test_data = pd.read_csv('./data_in/test_clean.csv')
testVec = vectorizer.transform(test_data['review'])
test_pred = model.predict(testVec)
print(f'test_pred : {test_pred}')

import os
if not os.path.exists('./data_out'):
    os.makedirs('./data_out')

myframe = pd.DataFrame({'id': test_data['id'], 'sentiment': test_pred})
myframe.to_csv('./data_out/model_tfidf_answer.csv', index=False, quoting=3)
