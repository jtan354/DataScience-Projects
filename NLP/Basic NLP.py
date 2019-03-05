#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn import metrics


# In[2]:


df = pd.read_csv("train.csv")


# In[3]:


df.head()


# In[4]:


df = df.drop(["itemid","image_path"], axis =1)


# In[5]:


df.head()


# In[6]:


X = df["title"]
y = df["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
cat_data = list(y_train)
title_data = list(X_train)


# In[7]:


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(title_data)
X_train_counts.shape


# In[8]:


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


# In[9]:


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, cat_data)


# In[10]:


X_test_counts = count_vect.transform(list(X_test))
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

y_pred = clf.predict(X_test_tfidf)
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
print('Accuracy: {:.5f}'.format(clf.score(X_test_tfidf, y_test)))
print(classification_report(y_test, clf.predict(X_test_tfidf)))


# In[11]:


from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(n_estimators=50, random_state=1)
rf.fit(X_train_tfidf,y_train)


# In[13]:


rf_pred = rf.predict(X_test_tfidf)
rf_count_misclassified = (y_test != rf_pred).sum()
print('Misclassified samples: {}'.format(rf_count_misclassified))
print('Accuracy: {:.5f}'.format(rf.score(X_test_tfidf, y_test)))
print(classification_report(y_test, rf.predict(X_test_tfidf)))


# In[ ]:




