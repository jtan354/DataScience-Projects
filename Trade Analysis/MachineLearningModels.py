#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


df = pd.read_csv('trading_data.csv', index_col='timestamp')
total_rows = len(df)
print(total_rows)
df.head()


# In[2]:


df.isnull().sum(axis=0)


# In[ ]:


import seaborn as sns
sns.pairplot(df)


# In[10]:


# set different Ys for prediction, drop ask and trade due to correlation
df_1s = df.drop(['_3s_side','_5s_side','ask_price','trade_price'], axis = 1)
df_1s_x = df_1s.drop(["_1s_side"], axis = 1)


# In[14]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_1s_x)
scaled_1s = pd.DataFrame(scaled_data, index=df_1s_x.index, columns=df_1s_x.columns)
scaled_1s['_1s_side'] = df_1s['_1s_side']


# In[16]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer

#imput missing values in sum_trade_1s and last_trade_time

fill_NaN = Imputer(missing_values=np.nan, strategy='mean', axis=1)
imputed_df_1s = pd.DataFrame(fill_NaN.fit_transform(scaled_1s))
imputed_df_1s.columns = scaled_1s.columns
imputed_df_1s.index = scaled_1s.index

X = imputed_df_1s.drop(['_1s_side'], axis =1)
y = imputed_df_1s['_1s_side']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, shuffle = False)


# In[17]:


from imblearn.over_sampling import SMOTENC
sm = SMOTENC(random_state=42, categorical_features=[6])
X_resampled, y_resampled = sm.fit_sample(X_train, y_train)


# In[18]:


print("Before OverSampling, counts of label '0': {}".format(sum(pd.DataFrame(y_train)['_1s_side']==0)))
print("Before OverSampling, counts of label '1': {}".format(sum(pd.DataFrame(y_train)['_1s_side']==1)))
print("Before OverSampling, counts of label '2': {}".format(sum(pd.DataFrame(y_train)['_1s_side']==2)))
print("After OverSampling, counts of label '0': {}".format(sum(pd.DataFrame(y_resampled)[0]==0)))
print("After OverSampling, counts of label '1': {}".format(sum(pd.DataFrame(y_resampled)[0]==1)))
print("After OverSampling, counts of label '2': {}".format(sum(pd.DataFrame(y_resampled)[0]==2)))


# In[19]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors = 461) #square root of n
knn.fit(X_resampled, y_resampled)

# Accuracy of k-NN model
y_pred = knn.predict(X_test)
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
print('Accuracy: {:.5f}'.format(knn.score(X_test, y_test)))

print(classification_report(y_test, knn.predict(X_test)))


# In[20]:


# Import the model we are using
from sklearn.ensemble import RandomForestClassifier
# Instantiate model with 10 decision trees
rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(X_resampled, y_resampled);


# In[28]:



# Use the forest's predict method on the test data
rf_pred = rf.predict(X_test)
count_misclassified = (y_test != rf_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
print('Accuracy: {:.5f}'.format(rf.score(X_test, y_test)))
print(classification_report(y_test, rf.predict(X_test)))


# In[22]:


from sklearn.tree import DecisionTreeClassifier 
dtree_model = DecisionTreeClassifier(max_depth = 6).fit(X_resampled, y_resampled) 
dtree_predictions = dtree_model.predict(X_test)
d_tree_count_misclassified = (y_test != dtree_predictions).sum()
print('Misclassified samples: {}'.format(d_tree_count_misclassified))
print('Accuracy: {:.5f}'.format(dtree_model.score(X_test, y_test)))
print(classification_report(y_test, dtree_model.predict(X_test)))


# In[26]:


# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'rbf', C = 10, gamma = 1.0).fit(X_resampled, y_resampled) 


# In[27]:


svm_predictions = svm_model_linear.predict(X_test)
svm_count_misclassified = (y_test != svm_predictions).sum()
print('Misclassified samples: {}'.format(svm_count_misclassified))
print('Accuracy: {:.5f}'.format(svm_model_linear.score(X_test, y_test)))
print(classification_report(y_test, svm_model_linear.predict(X_test)))


# In[35]:


from sklearn. ensemble import BaggingClassifier, AdaBoostClassifier, VotingClassifier
adb = AdaBoostClassifier(DecisionTreeClassifier(),n_estimators = 20, learning_rate = 1)
adb_model= adb.fit(X_resampled,y_resampled)


# In[37]:


adb_pred = adb_model.predict(X_test)
adb_count_misclassified = (y_test != adb_pred).sum()
print('Misclassified samples: {}'.format(adb_count_misclassified))
print('Accuracy: {:.5f}'.format(adb_model.score(X_test, y_test)))
print(classification_report(y_test, adb_model.predict(X_test)))


# In[41]:


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
dt = DecisionTreeClassifier()
svm = SVC(kernel = 'rbf', C = 10, gamma = 1.0 )
evc = VotingClassifier( estimators= [('lr',lr),('dt',dt),('svm',svm)], voting = 'hard')


# In[42]:


evc.fit(X_resampled,y_resampled)


# In[43]:


evc.score(X_test, y_test)


# In[ ]:




