

```python
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
```


```python
df = pd.read_csv("train.csv")
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemid</th>
      <th>title</th>
      <th>Category</th>
      <th>image_path</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>307504</td>
      <td>nyx sex bomb pallete natural palette</td>
      <td>0</td>
      <td>beauty_image/6b2e9cbb279ac95703348368aa65da09.jpg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>461203</td>
      <td>etude house precious mineral any cushion pearl...</td>
      <td>1</td>
      <td>beauty_image/20450222d857c9571ba8fa23bdedc8c9.jpg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3592295</td>
      <td>milani rose powder blush</td>
      <td>2</td>
      <td>beauty_image/6a5962bed605a3dd6604ca3a4278a4f9.jpg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4460167</td>
      <td>etude house baby sweet sugar powder</td>
      <td>3</td>
      <td>beauty_image/56987ae186e8a8e71fcc5a261ca485da.jpg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5853995</td>
      <td>bedak revlon color stay aqua mineral make up</td>
      <td>3</td>
      <td>beauty_image/9c6968066ebab57588c2f757a240d8b9.jpg</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.drop(["itemid","image_path"], axis =1)

```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nyx sex bomb pallete natural palette</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>etude house precious mineral any cushion pearl...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>milani rose powder blush</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>etude house baby sweet sugar powder</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bedak revlon color stay aqua mineral make up</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
X = df["title"]
y = df["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
cat_data = list(y_train)
title_data = list(X_train)
```


```python
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(title_data)
X_train_counts.shape
```




    (499961, 68538)




```python
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
```




    (499961, 68538)




```python
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, cat_data)
```


```python
X_test_counts = count_vect.transform(list(X_test))
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

y_pred = clf.predict(X_test_tfidf)
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
print('Accuracy: {:.5f}'.format(clf.score(X_test_tfidf, y_test)))
print(classification_report(y_test, clf.predict(X_test_tfidf)))
```

    Misclassified samples: 64854
    Accuracy: 0.61085
    

    C:\Users\TP_baseline\Anaconda3\lib\site-packages\sklearn\metrics\classification.py:1143: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.
      'precision', 'predicted', average, warn_for)
    C:\Users\TP_baseline\Anaconda3\lib\site-packages\sklearn\metrics\classification.py:1143: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.
      'precision', 'predicted', average, warn_for)
    

                  precision    recall  f1-score   support
    
               0       0.70      0.04      0.08       902
               1       0.63      0.47      0.54      7241
               2       0.85      0.66      0.74      2837
               3       0.71      0.88      0.79     20309
               4       0.60      0.70      0.65     10754
               5       0.65      0.77      0.70     13771
               6       0.00      0.00      0.00       517
               7       0.66      0.42      0.51      2929
               8       0.63      0.29      0.40      1517
               9       0.84      0.15      0.26      2060
              10       0.86      0.02      0.04       274
              11       0.73      0.06      0.11      1025
              12       0.71      0.87      0.79      5443
              13       0.77      0.23      0.35       739
              14       0.00      0.00      0.00       635
              15       0.00      0.00      0.00       136
              16       0.00      0.00      0.00       550
              17       0.00      0.00      0.00       696
              18       0.38      0.93      0.54     14312
              19       0.62      0.25      0.35      3371
              20       0.63      0.13      0.22      4969
              21       0.00      0.00      0.00      2607
              22       0.71      0.00      0.01      3717
              23       1.00      0.01      0.01       423
              24       0.00      0.00      0.00      1062
              25       0.69      0.68      0.69      8516
              26       0.57      0.55      0.56      8483
              27       0.91      0.13      0.22      4100
              28       0.61      0.04      0.07      1629
              29       1.00      0.01      0.02       794
              30       0.00      0.00      0.00       367
              31       0.80      0.86      0.83      6990
              32       0.81      0.90      0.85      7499
              33       0.90      0.52      0.65      1225
              34       0.82      0.66      0.73      3709
              35       0.38      0.61      0.47      7534
              36       0.50      0.00      0.01       274
              37       0.93      0.12      0.21       539
              38       0.89      0.40      0.55      1184
              39       1.00      0.01      0.02       167
              40       0.00      0.00      0.00        73
              41       0.84      0.88      0.86      4769
              42       0.86      0.66      0.75      2656
              43       0.85      0.36      0.51      1489
              44       1.00      0.01      0.02       238
              45       0.89      0.22      0.35       505
              46       1.00      0.04      0.09       178
              47       1.00      0.00      0.01       241
              48       1.00      0.01      0.02        92
              49       0.00      0.00      0.00       156
              50       0.00      0.00      0.00        65
              51       0.00      0.00      0.00        95
              52       0.00      0.00      0.00        20
              53       0.00      0.00      0.00       104
              54       0.00      0.00      0.00        64
              55       0.00      0.00      0.00        51
              56       0.00      0.00      0.00        42
              57       0.00      0.00      0.00        10
    
       micro avg       0.61      0.61      0.61    166654
       macro avg       0.53      0.25      0.27    166654
    weighted avg       0.64      0.61      0.57    166654
    
    

    C:\Users\TP_baseline\Anaconda3\lib\site-packages\sklearn\metrics\classification.py:1143: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.
      'precision', 'predicted', average, warn_for)
    


```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(n_estimators=50, random_state=1)
rf.fit(X_train_tfidf,y_train)
```




    RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=None, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=50, n_jobs=None,
                oob_score=False, random_state=1, verbose=0, warm_start=False)




```python
rf_pred = rf.predict(X_test_tfidf)
rf_count_misclassified = (y_test != rf_pred).sum()
print('Misclassified samples: {}'.format(rf_count_misclassified))
print('Accuracy: {:.5f}'.format(rf.score(X_test_tfidf, y_test)))
print(classification_report(y_test, rf.predict(X_test_tfidf)))
```

    Misclassified samples: 44001
    Accuracy: 0.73597
                  precision    recall  f1-score   support
    
               0       0.57      0.41      0.48       902
               1       0.76      0.64      0.70      7241
               2       0.84      0.87      0.86      2837
               3       0.86      0.89      0.88     20309
               4       0.69      0.75      0.72     10754
               5       0.76      0.78      0.77     13771
               6       0.50      0.42      0.45       517
               7       0.79      0.73      0.76      2929
               8       0.60      0.64      0.62      1517
               9       0.70      0.48      0.57      2060
              10       0.65      0.60      0.63       274
              11       0.64      0.55      0.60      1025
              12       0.78      0.91      0.84      5443
              13       0.66      0.61      0.63       739
              14       0.42      0.20      0.27       635
              15       0.44      0.21      0.29       136
              16       0.48      0.19      0.27       550
              17       0.43      0.18      0.26       696
              18       0.57      0.83      0.67     14312
              19       0.64      0.57      0.61      3371
              20       0.66      0.49      0.56      4969
              21       0.61      0.23      0.33      2607
              22       0.61      0.32      0.42      3717
              23       0.78      0.55      0.64       423
              24       0.64      0.18      0.28      1062
              25       0.75      0.78      0.77      8516
              26       0.65      0.74      0.69      8483
              27       0.72      0.54      0.62      4100
              28       0.71      0.55      0.62      1629
              29       0.67      0.56      0.61       794
              30       0.48      0.08      0.14       367
              31       0.84      0.89      0.87      6990
              32       0.84      0.91      0.87      7499
              33       0.83      0.94      0.88      1225
              34       0.79      0.83      0.81      3709
              35       0.69      0.48      0.57      7534
              36       0.79      0.91      0.85       274
              37       0.80      0.82      0.81       539
              38       0.82      0.92      0.87      1184
              39       0.78      0.81      0.80       167
              40       0.65      0.44      0.52        73
              41       0.85      0.92      0.89      4769
              42       0.84      0.91      0.88      2656
              43       0.75      0.87      0.81      1489
              44       0.87      0.85      0.86       238
              45       0.82      0.91      0.86       505
              46       0.87      0.93      0.90       178
              47       0.80      0.73      0.76       241
              48       0.76      0.82      0.79        92
              49       0.71      0.27      0.39       156
              50       0.80      0.88      0.84        65
              51       0.78      0.69      0.73        95
              52       0.62      0.40      0.48        20
              53       0.72      0.64      0.68       104
              54       0.68      0.62      0.65        64
              55       0.87      0.53      0.66        51
              56       0.69      0.43      0.53        42
              57       0.75      0.30      0.43        10
    
       micro avg       0.74      0.74      0.74    166654
       macro avg       0.71      0.62      0.65    166654
    weighted avg       0.73      0.74      0.73    166654
    
    


```python

```