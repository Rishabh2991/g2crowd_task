# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:46:09 2019

@author: Rishabh
"""

import numpy as np
import pandas as pd
df = pd.read_csv("companydata_test.txt",delimiter='~')
#print(df.Description)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.Description).toarray()
labels = df.Name
print(features.shape)


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


X_train, X_test, y_train, y_test = train_test_split(df['Description'], df['Type'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

print(y_test)
predict_ot = clf.predict(count_vect.transform(X_test))

print(predict_ot)
print('Test accuracy is {}'.format(accuracy_score(y_test, predict_ot)))

predict_ot = clf.predict(count_vect.transform([<SCRAPED DATA>]))
    
print(predict_ot)
print('Test accuracy is {}'.format(accuracy_score(["Finance"] ,predict_ot)))

