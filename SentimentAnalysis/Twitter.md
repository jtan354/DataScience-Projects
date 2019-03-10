

```python
import pandas as pd
```

## Reading the apple csv file into a pandas dataframe


```python
df = pd.read_csv('apple.csv' )
```

### More datatypes information on each column
- Look at the first 10 row
- Use describe() method
- Use info() method


```python
df.head(10)
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
      <th>_unit_id</th>
      <th>_golden</th>
      <th>_unit_state</th>
      <th>date</th>
      <th>id</th>
      <th>query</th>
      <th>text</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>623495513</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 19:30:03 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:The 10 best Steve Jobs emails ever...htt...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>1</th>
      <td>623495514</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 19:43:51 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>RT @JPDesloges: Why AAPL Stock Had a Mini-Flas...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>2</th>
      <td>623495515</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 19:50:28 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>My cat only chews @apple cords. Such an #Apple...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3</th>
      <td>623495516</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 20:26:34 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>I agree with @jimcramer that the #IndividualIn...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>4</th>
      <td>623495517</td>
      <td>False</td>
      <td>finalized</td>
      <td>Mon Dec 01 20:29:33 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Nobody expects the Spanish Inquisition #AAPL</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>5</th>
      <td>623495518</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 20:30:03 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:5 Rocket Stocks to Buy for December Gain...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>6</th>
      <td>623495519</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 20:32:45 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Top 3 all @Apple #tablets. Damn right! http://...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>7</th>
      <td>623495520</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 20:34:31 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>CNBCTV: #Apple's margins better than expected?...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>8</th>
      <td>623495521</td>
      <td>True</td>
      <td>golden</td>
      <td>Mon Dec 01 20:36:47 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Apple Inc. Flash Crash: What You Need to Know ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>9</th>
      <td>623495522</td>
      <td>False</td>
      <td>finalized</td>
      <td>Mon Dec 01 20:45:03 +0000 2014</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:This Presentation Shows What Makes The W...</td>
      <td>iphone</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3886 entries, 0 to 3885
    Data columns (total 8 columns):
    _unit_id       3886 non-null int64
    _golden        3886 non-null bool
    _unit_state    3886 non-null object
    date           3886 non-null object
    id             3886 non-null float64
    query          3886 non-null object
    text           3886 non-null object
    type           3886 non-null object
    dtypes: bool(1), float64(1), int64(1), object(5)
    memory usage: 216.4+ KB
    


```python
df.describe()
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
      <th>_unit_id</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.886000e+03</td>
      <td>3.886000e+03</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.234975e+08</td>
      <td>5.410039e+17</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.171906e+03</td>
      <td>7.942752e+14</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6.234955e+08</td>
      <td>5.400000e+17</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.234965e+08</td>
      <td>5.400000e+17</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.234975e+08</td>
      <td>5.410000e+17</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.234984e+08</td>
      <td>5.420000e+17</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6.235173e+08</td>
      <td>5.420000e+17</td>
    </tr>
  </tbody>
</table>
</div>



### Drop unneccessary columns


```python
df.drop(columns= ["_unit_id","_golden","_unit_state","id","query"])
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
      <th>date</th>
      <th>text</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mon Dec 01 19:30:03 +0000 2014</td>
      <td>#AAPL:The 10 best Steve Jobs emails ever...htt...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mon Dec 01 19:43:51 +0000 2014</td>
      <td>RT @JPDesloges: Why AAPL Stock Had a Mini-Flas...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mon Dec 01 19:50:28 +0000 2014</td>
      <td>My cat only chews @apple cords. Such an #Apple...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mon Dec 01 20:26:34 +0000 2014</td>
      <td>I agree with @jimcramer that the #IndividualIn...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mon Dec 01 20:29:33 +0000 2014</td>
      <td>Nobody expects the Spanish Inquisition #AAPL</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mon Dec 01 20:30:03 +0000 2014</td>
      <td>#AAPL:5 Rocket Stocks to Buy for December Gain...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mon Dec 01 20:32:45 +0000 2014</td>
      <td>Top 3 all @Apple #tablets. Damn right! http://...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Mon Dec 01 20:34:31 +0000 2014</td>
      <td>CNBCTV: #Apple's margins better than expected?...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Mon Dec 01 20:36:47 +0000 2014</td>
      <td>Apple Inc. Flash Crash: What You Need to Know ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mon Dec 01 20:45:03 +0000 2014</td>
      <td>#AAPL:This Presentation Shows What Makes The W...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Mon Dec 01 20:46:01 +0000 2014</td>
      <td>WTF MY BATTERY WAS 31% ONE SECOND AGO AND NOW ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Mon Dec 01 20:47:12 +0000 2014</td>
      <td>Apple Watch Tops Search Engine List of Best We...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Mon Dec 01 21:00:15 +0000 2014</td>
      <td>The Best-Designed #iPhone #Apps In the World, ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Mon Dec 01 21:03:32 +0000 2014</td>
      <td>RT @peterpham: Bought my @AugustSmartLock at t...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Mon Dec 01 21:09:50 +0000 2014</td>
      <td>@apple Contact sync between Yosemite and iOS8 ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Mon Dec 01 21:29:45 +0000 2014</td>
      <td>#aapl @applenws Thanks to the non factual dumb...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Mon Dec 01 21:35:14 +0000 2014</td>
      <td>WARNING IF YOU BUY AN IPHONE 5S UNLOCKED FROM ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Mon Dec 01 21:52:04 +0000 2014</td>
      <td>@Apple John Cantlie has been a prisoner of ISI...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Mon Dec 01 21:53:12 +0000 2014</td>
      <td>@apple- thanks for xtra checkin at upper wests...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Mon Dec 01 22:22:09 +0000 2014</td>
      <td>Why #AAPL Stock Had a Mini-Flash Crash Today: ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Mon Dec 01 23:03:01 +0000 2014</td>
      <td>$AAPL dip only momentarily....just an aberrati...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Mon Dec 01 23:12:40 +0000 2014</td>
      <td>The JH Hines Staff with their newly issued @ap...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Mon Dec 01 23:43:14 +0000 2014</td>
      <td>@robconeybeer: You need an IP portfolio to def...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Mon Dec 01 23:55:55 +0000 2014</td>
      <td>@Apple, For the love of GAWD, CENTER the '1'on...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Tue Dec 02 00:06:05 +0000 2014</td>
      <td>i get the storage almost full notification lit...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Tue Dec 02 00:14:25 +0000 2014</td>
      <td>I had to do made the #switch from iPhone 6 to ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Tue Dec 02 00:15:11 +0000 2014</td>
      <td>@ me RT @101Baemations: Can't stand those ppl ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Tue Dec 02 00:15:14 +0000 2014</td>
      <td>Justice Department cites 18th century federal ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Tue Dec 02 00:15:16 +0000 2014</td>
      <td>Latest Apple Products Leading in Efficiency ht...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Tue Dec 02 00:15:26 +0000 2014</td>
      <td>RT @thehill: Justice Department cites 18th cen...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3856</th>
      <td>Tue Dec 09 21:17:52 +0000 2014</td>
      <td>@NickM538 @Apple tell them how ya really feel</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3857</th>
      <td>Tue Dec 09 21:20:21 +0000 2014</td>
      <td>why isnt group facetime a thing @apple wtf</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>3858</th>
      <td>Tue Dec 09 21:21:00 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3859</th>
      <td>Tue Dec 09 21:21:00 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3860</th>
      <td>Tue Dec 09 21:21:00 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>3861</th>
      <td>Tue Dec 09 21:21:00 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>3862</th>
      <td>Tue Dec 09 21:21:01 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3863</th>
      <td>Tue Dec 09 21:21:01 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3864</th>
      <td>Tue Dec 09 21:21:03 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3865</th>
      <td>Tue Dec 09 21:21:04 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3866</th>
      <td>Tue Dec 09 21:21:04 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3867</th>
      <td>Tue Dec 09 21:21:05 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3868</th>
      <td>Tue Dec 09 21:21:05 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3869</th>
      <td>Tue Dec 09 21:21:07 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3870</th>
      <td>Tue Dec 09 21:21:07 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3871</th>
      <td>Tue Dec 09 21:21:09 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3872</th>
      <td>Tue Dec 09 21:21:09 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3873</th>
      <td>Tue Dec 09 21:21:10 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3874</th>
      <td>Tue Dec 09 21:21:10 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3875</th>
      <td>Tue Dec 09 21:21:11 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>3876</th>
      <td>Tue Dec 09 21:21:12 +0000 2014</td>
      <td>Apple Is Warming Up To Social Media: Apple is ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3877</th>
      <td>Tue Dec 09 21:23:33 +0000 2014</td>
      <td>Being held hostage at @apple - They are replac...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3878</th>
      <td>Tue Dec 09 21:24:22 +0000 2014</td>
      <td>RT @shannonmmiller: Love the @Apple is support...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3879</th>
      <td>Tue Dec 09 21:27:06 +0000 2014</td>
      <td>Tim Cook Met With Jesse Jackson for 'Positive ...</td>
      <td>ipad</td>
    </tr>
    <tr>
      <th>3880</th>
      <td>Tue Dec 09 21:28:07 +0000 2014</td>
      <td>hey @apple is it normal for my laptop charger ...</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>3881</th>
      <td>Tue Dec 09 22:08:53 +0000 2014</td>
      <td>(Via FC) Apple Is Warming Up To Social Media -...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3882</th>
      <td>Tue Dec 09 22:18:27 +0000 2014</td>
      <td>RT @MMLXIV: there is no avocado emoji may I as...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3883</th>
      <td>Tue Dec 09 23:45:59 +0000 2014</td>
      <td>@marcbulandr I could not agree more. Between @...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3884</th>
      <td>Wed Dec 10 00:48:10 +0000 2014</td>
      <td>My iPhone 5's photos are no longer downloading...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>3885</th>
      <td>Tue Dec 09 09:01:25 +0000 2014</td>
      <td>RT @SwiftKey: We're so excited to be named to ...</td>
      <td>ipad</td>
    </tr>
  </tbody>
</table>
<p>3886 rows × 3 columns</p>
</div>



#### Realise that the date format is in text. We should change it to a proper datetime format for ease of data representation in the future! Use pd.to_datetime() method


```python
df["date"]=pd.to_datetime(df["date"])
```

#### Notice that the date data type has been changed to datetime64 which is what we wanted


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3886 entries, 0 to 3885
    Data columns (total 8 columns):
    _unit_id       3886 non-null int64
    _golden        3886 non-null bool
    _unit_state    3886 non-null object
    date           3886 non-null datetime64[ns]
    id             3886 non-null float64
    query          3886 non-null object
    text           3886 non-null object
    type           3886 non-null object
    dtypes: bool(1), datetime64[ns](1), float64(1), int64(1), object(4)
    memory usage: 216.4+ KB
    

# Sentiment prediction
---

#### Using textblob, a python libray with a simple text classification model, to analyze the sentiments of each tweets. It has a polarity score of -1 to 1, -1 being most negative and 1 being most positive.


```python

!pip install textblob
from textblob import TextBlob
```

    Collecting textblob
      Downloading https://files.pythonhosted.org/packages/60/f0/1d9bfcc8ee6b83472ec571406bd0dd51c0e6330ff1a51b2d29861d389e85/textblob-0.15.3-py2.py3-none-any.whl (636kB)
    Requirement already satisfied: nltk>=3.1 in c:\users\tp_baseline\anaconda3\lib\site-packages (from textblob) (3.4)
    Requirement already satisfied: six in c:\users\tp_baseline\anaconda3\lib\site-packages (from nltk>=3.1->textblob) (1.12.0)
    Requirement already satisfied: singledispatch in c:\users\tp_baseline\anaconda3\lib\site-packages (from nltk>=3.1->textblob) (3.4.0.3)
    Installing collected packages: textblob
    Successfully installed textblob-0.15.3
    

We can obtain sentiments of each string by accessing the TextBlob method:

    TextBlob('The service is horrible!').sentiment.polarity
Will give us a -1.0 score. 

Now try finding out the sentiment of the 2 strings:
- `'The apple product is horrible!'`
- `'What an awesome apple laptop!'`


```python
TextBlob('This a not so good product').sentiment.polarity
```




    0.7



#### We create a column named  *sentiment* which is the sentiment scoring of the related row's text



```python
df["sentiment"]=df.apply(lambda row: TextBlob(row["text"]).sentiment.polarity, axis = 1)
df.head(30)
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
      <th>_unit_id</th>
      <th>_golden</th>
      <th>_unit_state</th>
      <th>date</th>
      <th>id</th>
      <th>query</th>
      <th>text</th>
      <th>type</th>
      <th>sentiment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>623495513</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 19:30:03</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:The 10 best Steve Jobs emails ever...htt...</td>
      <td>iphone</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>623495514</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 19:43:51</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>RT @JPDesloges: Why AAPL Stock Had a Mini-Flas...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>623495515</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 19:50:28</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>My cat only chews @apple cords. Such an #Apple...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>623495516</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:26:34</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>I agree with @jimcramer that the #IndividualIn...</td>
      <td>iphone</td>
      <td>0.650000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>623495517</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 20:29:33</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Nobody expects the Spanish Inquisition #AAPL</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>623495518</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:30:03</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:5 Rocket Stocks to Buy for December Gain...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>623495519</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:32:45</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Top 3 all @Apple #tablets. Damn right! http://...</td>
      <td>iphone</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>7</th>
      <td>623495520</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:34:31</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>CNBCTV: #Apple's margins better than expected?...</td>
      <td>iphone</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>623495521</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:36:47</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Apple Inc. Flash Crash: What You Need to Know ...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>623495522</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 20:45:03</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#AAPL:This Presentation Shows What Makes The W...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>623495523</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:46:01</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>WTF MY BATTERY WAS 31% ONE SECOND AGO AND NOW ...</td>
      <td>macbook</td>
      <td>-0.333333</td>
    </tr>
    <tr>
      <th>11</th>
      <td>623495524</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:47:12</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Apple Watch Tops Search Engine List of Best We...</td>
      <td>iphone</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>623495525</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 21:00:15</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>The Best-Designed #iPhone #Apps In the World, ...</td>
      <td>ipad</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>623495526</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 21:03:32</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>RT @peterpham: Bought my @AugustSmartLock at t...</td>
      <td>iphone</td>
      <td>0.875000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>623495527</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 21:09:50</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@apple Contact sync between Yosemite and iOS8 ...</td>
      <td>macbook</td>
      <td>-0.027778</td>
    </tr>
    <tr>
      <th>15</th>
      <td>623495528</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 21:29:45</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>#aapl @applenws Thanks to the non factual dumb...</td>
      <td>iphone</td>
      <td>0.008333</td>
    </tr>
    <tr>
      <th>16</th>
      <td>623495529</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 21:35:14</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>WARNING IF YOU BUY AN IPHONE 5S UNLOCKED FROM ...</td>
      <td>ipad</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>623495530</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 21:52:04</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@Apple John Cantlie has been a prisoner of ISI...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>623495531</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 21:53:12</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@apple- thanks for xtra checkin at upper wests...</td>
      <td>macbook</td>
      <td>-0.033333</td>
    </tr>
    <tr>
      <th>19</th>
      <td>623495532</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 22:22:09</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Why #AAPL Stock Had a Mini-Flash Crash Today: ...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>623495533</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 23:03:01</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>$AAPL dip only momentarily....just an aberrati...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>623495534</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 23:12:40</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>The JH Hines Staff with their newly issued @ap...</td>
      <td>ipad</td>
      <td>0.136364</td>
    </tr>
    <tr>
      <th>22</th>
      <td>623495535</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 23:43:14</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@robconeybeer: You need an IP portfolio to def...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>623495536</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 23:55:55</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@Apple, For the love of GAWD, CENTER the '1'on...</td>
      <td>iphone</td>
      <td>0.075000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>623495537</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-02 00:06:05</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>i get the storage almost full notification lit...</td>
      <td>iphone</td>
      <td>0.350000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>623495538</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-02 00:14:25</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>I had to do made the #switch from iPhone 6 to ...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>623495539</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-02 00:15:11</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@ me RT @101Baemations: Can't stand those ppl ...</td>
      <td>iphone</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>623495540</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-02 00:15:14</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Justice Department cites 18th century federal ...</td>
      <td>ipad</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>623495541</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-02 00:15:16</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>Latest Apple Products Leading in Efficiency ht...</td>
      <td>ipad</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>623495542</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-02 00:15:26</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>RT @thehill: Justice Department cites 18th cen...</td>
      <td>ipad</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Let's understand the public's sentiment of Apple the past 10 days

Plotting the frequency of negative and positive tweets by date (line charts representing 2 lines, frequency of negative and positive tweets)


```python
%matplotlib inline
import matplotlib.pyplot as plt
df_negative = df[df['sentiment']<0]
df_negative['date'] = df_negative.apply(lambda row: row['date'].day, axis =1)
df_negative = df_negative.groupby(['date']).count()
df_positive = df[df['sentiment']>0]
df_positive['date'] = df_positive.apply(lambda row: row['date'].day, axis =1)
df_positive = df_positive.groupby(['date']).count()
plt.plot(df_negative.index, df_negative['sentiment'], color = 'r')
plt.plot(df_positive.index, df_positive['sentiment'], color = 'b')
plt.legend(['negative', 'positive'], loc='upper left')
plt.show()
```

    C:\Users\TP_baseline\Anaconda3\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    C:\Users\TP_baseline\Anaconda3\lib\site-packages\ipykernel_launcher.py:7: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      import sys
    


![png](output_21_1.png)


### Due to the sharp spike in negative sentiments from the public, lets find out which type of product has been drawing negative feedback

Plot a bar chart to show a breakdown of number of negative feedbacks by `type`


```python
df_negative = df[df['sentiment']<0]
count = df_negative['type'].value_counts()
width = 1/1.5
plt.bar(count.index, count.values, width, color = "red")
plt.xlabel('Product')
plt.ylabel('Count')

plt.title('Figure 1:\n Products with negative sentiment')
```




    Text(0.5, 1.0, 'Figure 1:\n Products with negative sentiment')




![png](output_23_1.png)


## For a more comprehensive analysis, wordcloud is used as well. 

Install relevant libraries and import them


```python
!pip install wordcloud
from wordcloud import WordCloud
import operator
```

    Collecting wordcloud
      Using cached https://files.pythonhosted.org/packages/23/4e/1254d26ce5d36facdcbb5820e7e434328aed68e99938c75c9d4e2fee5efb/wordcloud-1.5.0-cp37-cp37m-win_amd64.whl
    Requirement already satisfied: pillow in c:\users\tp_baseline\anaconda3\lib\site-packages (from wordcloud) (5.3.0)
    Requirement already satisfied: numpy>=1.6.1 in c:\users\tp_baseline\anaconda3\lib\site-packages (from wordcloud) (1.16.2)
    Installing collected packages: wordcloud
    Successfully installed wordcloud-1.5.0
    

defining stopwords ( words that may not be significant like 'the', 'a' and etc...)


```python
stopwords = ['RT','all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
```

1. Assign negative rows to a dataframe defined as df_negative
2. Create a new column `textlist` which splits the text into individual words in a list (make sure all words are in lower cap). Hint: .str.lower().str.split() 


```python
df_negative = df[df['sentiment']<0].reset_index()
df_negative.reset_index(inplace = True)
df_negative['textlist']=df_negative['text'].str.lower().str.split()
df_negative.head()
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
      <th>level_0</th>
      <th>index</th>
      <th>_unit_id</th>
      <th>_golden</th>
      <th>_unit_state</th>
      <th>date</th>
      <th>id</th>
      <th>query</th>
      <th>text</th>
      <th>type</th>
      <th>sentiment</th>
      <th>textlist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>10</td>
      <td>623495523</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 20:46:01</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>WTF MY BATTERY WAS 31% ONE SECOND AGO AND NOW ...</td>
      <td>macbook</td>
      <td>-0.333333</td>
      <td>[wtf, my, battery, was, 31%, one, second, ago,...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>14</td>
      <td>623495527</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-01 21:09:50</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@apple Contact sync between Yosemite and iOS8 ...</td>
      <td>macbook</td>
      <td>-0.027778</td>
      <td>[@apple, contact, sync, between, yosemite, and...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>18</td>
      <td>623495531</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-01 21:53:12</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@apple- thanks for xtra checkin at upper wests...</td>
      <td>macbook</td>
      <td>-0.033333</td>
      <td>[@apple-, thanks, for, xtra, checkin, at, uppe...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>47</td>
      <td>623495560</td>
      <td>True</td>
      <td>golden</td>
      <td>2014-12-02 00:34:51</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@apple U need to get ur fucking shit together ...</td>
      <td>macbook</td>
      <td>-0.200000</td>
      <td>[@apple, u, need, to, get, ur, fucking, shit, ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>48</td>
      <td>623495561</td>
      <td>False</td>
      <td>finalized</td>
      <td>2014-12-02 00:38:41</td>
      <td>5.400000e+17</td>
      <td>#AAPL OR @Apple</td>
      <td>@thehill @Apple Wish we could prosecute the ad...</td>
      <td>ipad</td>
      <td>-0.400000</td>
      <td>[@thehill, @apple, wish, we, could, prosecute,...</td>
    </tr>
  </tbody>
</table>
</div>



Create a dictionary that counts the frequency of each word in column `textlist` make sure the word is not in the list stopwords


```python
worddic = {}

for words in df_negative['textlist']:
    for word in words:
        if word.lower() not in stopwords:
            if word not in worddic:
                worddic[word] = 1
            else:
                worddic[word]+=1

worddic
```




    {'wtf': 23,
     'battery': 13,
     '31%': 1,
     'one': 14,
     'second': 4,
     'ago': 2,
     '29%': 1,
     '@apple': 651,
     'contact': 3,
     'sync': 3,
     'yosemite': 6,
     'ios8': 5,
     'seriously': 3,
     'screwed': 1,
     'up.': 4,
     'used': 3,
     'much': 10,
     'stable': 1,
     'past.': 1,
     '#icloud': 2,
     '#isync': 1,
     '@apple-': 1,
     'thanks': 10,
     'xtra': 1,
     'checkin': 1,
     'upper': 1,
     'westside': 1,
     'store-': 1,
     'appointments': 1,
     'running': 2,
     'almost': 3,
     '50': 2,
     'minutes': 4,
     'late?': 2,
     'u': 22,
     'need': 12,
     'get': 35,
     'ur': 13,
     'fucking': 40,
     'shit': 70,
     'together': 18,
     'let': 14,
     'txt': 2,
     'youtube': 2,
     '@thehill': 2,
     'wish': 3,
     'could': 6,
     'prosecute': 2,
     'admin': 2,
     'violation': 2,
     'privacy': 2,
     'criminal': 2,
     'search': 4,
     'seizure': 2,
     'hey': 21,
     'fuck': 88,
     "doesn't": 10,
     'people': 4,
     'explain': 1,
     'precautions': 1,
     'buying': 2,
     'expensive': 2,
     'laptop': 4,
     '@quailman_': 1,
     'bored': 1,
     'huh': 1,
     'die': 4,
     'hard': 16,
     'customer,': 3,
     'must': 3,
     'say': 4,
     'truly': 3,
     'displeased': 3,
     'customer': 9,
     'service': 11,
     'given': 5,
     'today.': 3,
     '#badservice': 3,
     '#apple': 20,
     'made': 4,
     'clear': 2,
     'today': 4,
     'worth': 1,
     'measly': 1,
     '$79!!': 1,
     'employee': 2,
     'gave': 2,
     'mis': 1,
     'info': 2,
     'stand': 3,
     'behind': 4,
     'buy': 11,
     'round': 1,
     'lot': 3,
     'open': 4,
     'mt': 2,
     '@wsjd': 1,
     '#aapl': 72,
     'stock': 7,
     'briefly': 1,
     'dove': 1,
     '6.4%': 2,
     'analysts': 2,
     'sure': 5,
     'http://t.co/f6e73ejuje': 1,
     'http://t.co/2qqvmwootv': 1,
     "daughter's": 1,
     '#ipod': 5,
     'stolen.': 2,
     'thief:': 1,
     'try': 4,
     'working': 5,
     'earn': 1,
     '-': 13,
     'like': 22,
     'daughter': 1,
     'hers.': 1,
     '#losingfaithinpeople': 1,
     'rt': 209,
     '@tinfoiltricorn:': 1,
     'game': 10,
     '#traders': 1,
     'play': 4,
     'name': 1,
     '#market': 5,
     '#liquidity': 1,
     '#hft': 1,
     '#darkpools': 1,
     '#stock': 1,
     '#trading': 4,
     '#algorithms': 1,
     'http://t.co/lakjpr89s8': 1,
     'sooooo': 4,
     'annoyed.': 1,
     'restore': 2,
     'back': 9,
     'lost': 3,
     'voice': 1,
     'mails.': 1,
     'needed': 1,
     'keep': 6,
     'those.': 1,
     'broke': 5,
     '3rd': 1,
     'charger': 14,
     'month.': 2,
     '@iphone4': 1,
     'oh': 4,
     "it's": 37,
     'fair': 1,
     'think': 8,
     "you're": 3,
     'really': 14,
     'mean': 7,
     'hate': 30,
     'ios': 12,
     '8': 3,
     'capitalizes': 1,
     'random': 2,
     'words': 5,
     'dont': 4,
     'wanna': 1,
     'give': 4,
     'emphasis': 1,
     'stupid': 10,
     'word': 2,
     'tha': 1,
     'sentence': 1,
     'self': 1,
     'http://t.co/xrxxk0rdot': 1,
     '#nasdaq100': 3,
     '#recent': 4,
     '#exit': 4,
     '#4:': 4,
     'sold': 5,
     '$aapl': 26,
     'long': 9,
     '10.49%': 4,
     '#gain': 4,
     '20': 6,
     'days.': 4,
     '#forex': 4,
     '#stocks': 4,
     'chayton': 1,
     'falke': 1,
     'chaytonfalke': 1,
     ':#nasdaq100': 1,
     '#trading...': 1,
     'phones': 4,
     'charging': 3,
     'hour': 3,
     'keeps': 6,
     'losing': 2,
     'percentage??': 2,
     'completely': 5,
     'dead': 2,
     'blacked': 1,
     '2': 10,
     'days': 5,
     '&amp;': 13,
     'finally': 3,
     'opened': 1,
     'inside': 1,
     'fixed': 2,
     'it.': 5,
     'hire': 1,
     '@toricolelli:': 1,
     'changing': 2,
     'yet': 3,
     'another': 5,
     'duck...thanks.': 1,
     '@brwnskin_beauti': 1,
     'cause': 2,
     'breaking': 3,
     'music': 12,
     'yo!': 1,
     'auto': 3,
     'correct': 3,
     'gotta': 4,
     'stop!!!': 1,
     'right': 2,
     'send': 6,
     'those**': 1,
     'pick': 1,
     'slack': 1,
     'boys': 2,
     'faggots': 2,
     'course': 1,
     "that's": 2,
     'mother': 1,
     '@': 5,
     'kinda': 3,
     'gay': 2,
     'print': 1,
     'ketosis': 1,
     'game***': 1,
     'bitches': 2,
     'trying': 11,
     'tonight!': 1,
     '@dremacsamillion:': 1,
     '@whosflyy__': 1,
     'gams': 1,
     'night': 5,
     'gawd': 1,
     '@bella_bong_:': 1,
     '@disney': 1,
     "can't": 19,
     'version': 3,
     'alone': 2,
     'actually': 5,
     'star': 3,
     'wars': 1,
     '@itunesmovies': 1,
     '#stupid': 1,
     '#lame': 1,
     '#starwars': 1,
     '@tim_cook': 5,
     'perhaps': 1,
     'less': 6,
     'malleable': 1,
     'metal': 1,
     'shell': 1,
     '#iphone6splus.': 1,
     '#noticedsomecurve': 1,
     'drop': 1,
     'audio': 1,
     'rendition': 1,
     'requirement': 1,
     'apps?': 1,
     'users': 4,
     'stores': 5,
     'want': 7,
     'platforms': 1,
     "don't": 15,
     'know': 7,
     'time': 9,
     '#pages': 1,
     'ate': 1,
     'edits.': 1,
     '700bn?': 1,
     '#amateurs': 1,
     '#fail': 9,
     '#iwantjobsback': 1,
     'feel': 3,
     'phone': 59,
     ':(': 7,
     'iphone': 53,
     '5': 6,
     'chargers': 15,
     'horrendous!': 1,
     '#brokenchargerprobs': 1,
     'secret': 1,
     'life': 12,
     'steve': 8,
     'jobs': 4,
     '46': 1,
     'seconds.': 1,
     '#motivation': 1,
     'late': 8,
     'ceo': 1,
     'http://t.co/7uoykec9yn': 1,
     '@hammerarcade': 1,
     'makes': 5,
     'sad': 1,
     ';-;': 1,
     'rood': 1,
     'earphones': 2,
     'bad.': 1,
     'world': 2,
     'good': 4,
     'idea': 7,
     'p': 1,
     'http://t.co/x7ligaqeg5': 1,
     'http://t.co/ihr2ogza6s': 1,
     'dying': 4,
     'fast': 1,
     'phone?': 2,
     'holy': 1,
     'missed': 3,
     'obama': 1,
     '#nasdaq': 2,
     '#nyse': 1,
     '#dowj': 1,
     'http://t.co/zmkp6xyjk4': 1,
     '#iphone': 8,
     '@iphone': 4,
     '#iphone4s': 1,
     '#iphone4problems': 1,
     'someone': 5,
     'help': 9,
     'works': 4,
     'apple': 65,
     'job': 1,
     'cunts': 1,
     '@apple,': 13,
     'synching': 1,
     'notes': 1,
     'icloud': 3,
     'pages': 1,
     'unusable.': 2,
     'easier.': 1,
     'change': 3,
     'since': 10,
     'updating': 2,
     '#ipad': 2,
     '#os': 1,
     '#bug': 2,
     'delete': 4,
     'videos': 1,
     'free': 4,
     'memory': 1,
     'forcing...': 1,
     'http://t.co/ajddtf19nn': 1,
     'morgan': 1,
     'stanley': 1,
     'negative': 1,
     'tech': 3,
     'sector': 1,
     'http://t.co/warhey9ueh': 1,
     'bbc': 1,
     'news': 1,
     'evidence': 1,
     'trial': 2,
     'http://t.co/i6dxppuwjy': 1,
     'alarm': 4,
     'set': 3,
     'ringer': 1,
     'refused': 1,
     'work': 6,
     'technology': 2,
     'news:': 1,
     'feature': 2,
     'unseen': 1,
     '#stevejobs': 4,
     'video': 3,
     'deposition': 1,
     'http://t.co/yvyotpdmzp': 1,
     'figured': 2,
     '#memory': 1,
     'issue': 3,
     '#ipad.': 1,
     'wasnt': 1,
     'new': 23,
     'hidden': 1,
     'folder': 1,
     'images...': 1,
     'http://t.co/vekie3qldp': 1,
     '#aapl:': 1,
     'audio:': 1,
     'sales': 2,
     'due;': 1,
     'lawsuit': 4,
     'heads': 1,
     'court...http://t.co/kvb1l61oln': 1,
     'dear': 12,
     'replace': 7,
     'sucks': 11,
     '@laurrynk:': 2,
     '@thisdueemarco': 1,
     'thats': 1,
     'annoying,': 1,
     'never': 5,
     'stuff': 6,
     'first': 1,
     'time.': 4,
     'lower': 2,
     'analyst': 2,
     'sees': 3,
     'risk': 3,
     'sharp': 2,
     'production': 3,
     'cuts': 2,
     '6': 24,
     'plus': 7,
     'q1': 2,
     'http://t.co/sqetceojpq': 2,
     '@jpdesloges:': 4,
     'realmac': 1,
     'software': 5,
     'launches': 2,
     "'typed',": 1,
     'markdown': 1,
     'writing': 1,
     'app': 7,
     'featuring': 1,
     'minimal': 2,
     'interface': 1,
     '[mac': 2,
     'blog]': 4,
     'http://t.co/3hq47gile6': 1,
     '#cnbc': 2,
     'make': 21,
     'poor': 5,
     '#cl': 1,
     'got': 8,
     'slammed': 1,
     'yesterday.yesterday.': 1,
     'pisini': 1,
     'please': 11,
     'put': 4,
     'clown': 2,
     'shoes': 1,
     'report': 1,
     '#aapl:how': 1,
     'remove': 2,
     'pay': 10,
     'credit': 2,
     'cards': 1,
     'remotely': 1,
     'http://t.co/jpd3hwdeee...http://t.co/7xgbbp7cjw': 1,
     "'keep": 1,
     "newer'": 1,
     'transferring': 1,
     'files': 3,
     'local': 2,
     'drive': 2,
     'server.': 1,
     '@sony': 1,
     '#e-paper': 1,
     'fes': 1,
     '#watch': 1,
     'coolest': 1,
     'piece': 4,
     '#wearable': 1,
     '#tech': 3,
     'yet,': 1,
     'sorry': 4,
     'http://t.co/542rsjsmkf': 1,
     '@luchanglu': 1,
     'via': 8,
     '@bustle': 1,
     'loses': 7,
     'ground': 3,
     'google': 5,
     'education': 1,
     'tablet': 2,
     'http://t.co/ap0c3ehzle': 1,
     'mac': 5,
     'slow': 7,
     'lately': 3,
     '?': 4,
     '@gregsherry': 1,
     'successes': 1,
     'fails': 4,
     '@southwestair': 1,
     'examples': 1,
     'http://t.co/jg7jp6l7zd': 1,
     '@dkusnetzky': 1,
     '#custserv': 1,
     '#cx': 1,
     '#cem': 1,
     'upgrade': 3,
     'ruined': 1,
     'god': 6,
     'damned': 1,
     'ide': 1,
     'pieces': 5,
     '@apple!': 3,
     'damnit': 2,
     'man!': 2,
     'happened?': 1,
     '@khaleel': 1,
     'cnbctv:': 2,
     '#cramer:': 2,
     'trading': 1,
     'suckers': 1,
     'http://t.co/cpmnqxdwit': 1,
     'chromecast': 1,
     'leapfrogs': 2,
     'tv': 3,
     'aging': 3,
     'media': 4,
     'player': 3,
     'rivals': 2,
     'http://t.co/14uhvycp6b': 1,
     'freezing': 6,
     '@unstanningzarry:': 1,
     'inc.': 5,
     'co-founder': 2,
     "'testifies'": 1,
     'itunes': 8,
     'case': 6,
     'http://t.co/umrfdsvfzo': 1,
     'happy': 3,
     '@appstore': 3,
     'backwards': 1,
     'compatibility': 1,
     'given.': 1,
     'apps': 8,
     'aperture??': 1,
     'money': 4,
     'grab?': 1,
     'yesterday.': 2,
     'deutsche': 1,
     'bank': 2,
     "iphone's": 2,
     "'sharp": 1,
     "cuts'": 1,
     'http://t.co/qhlvagzjku': 1,
     '@google': 3,
     '#chromecast': 1,
     '#tv': 1,
     'http://t.co/uks4uydeki': 1,
     'plz': 1,
     'kill': 2,
     'verizon': 1,
     'soooo': 1,
     'weird': 3,
     'passcodes': 1,
     'synchronized': 1,
     'locations': 1,
     'everything': 2,
     'strikes': 1,
     'somewhat': 1,
     'sent': 2,
     'brand': 2,
     'without': 4,
     'latest': 1,
     'on.': 2,
     'old': 3,
     'stuff.': 1,
     'dead:': 1,
     'ipods': 2,
     'drag': 2,
     'court': 1,
     'http://t.co/8cqmzyqegt': 1,
     'too.': 2,
     '@msnarcissistic': 1,
     'microphone': 1,
     'imessage': 2,
     'take': 6,
     '@apple.': 6,
     'kindly': 1,
     '.m4a': 1,
     'format.': 1,
     'regards,': 2,
     'listeners': 1,
     'everywhere.': 1,
     '@uberfacts': 1,
     '100': 1,
     'reasons': 1,
     '4s.': 1,
     '@sometimesboring': 1,
     'also': 3,
     'even': 11,
     'live': 1,
     'kirkby': 1,
     "there's": 1,
     'movie': 2,
     'match': 1,
     '/': 3,
     'remove.': 1,
     'trailer.': 1,
     'annoying': 7,
     'siri': 3,
     'bull': 1,
     'telling': 2,
     'gonna': 2,
     'rain': 5,
     'da': 4,
     '.@apple': 5,
     'macmail': 1,
     'os': 4,
     'x': 2,
     '#yosemite': 7,
     'giving': 3,
     'alternative': 2,
     'email': 7,
     'program': 2,
     'there?': 1,
     '#yosemiteproblems': 3,
     'autocorrect': 2,
     'changes': 1,
     'actual': 5,
     'spell': 2,
     'wrong': 14,
     'it?': 1,
     'yall': 12,
     'niggas': 3,
     'hell': 4,
     '5gbs': 1,
     "'other'": 1,
     'data': 1,
     '@apple?????????': 1,
     '2/': 1,
     'announcement': 1,
     '@samsung': 2,
     'supporters': 1,
     'criticized': 1,
     "'following'": 1,
     'samsung': 4,
     'large': 1,
     'screen': 8,
     'game.': 2,
     'middle': 1,
     'finger': 2,
     'emoji': 2,
     'ignore': 1,
     'niggaz': 1,
     'talk': 2,
     'wit': 2,
     'single': 1,
     'sign': 2,
     'utterly': 1,
     'broken': 9,
     'wifi': 1,
     'driver:': 1,
     'air': 1,
     'sitting': 1,
     'lap': 1,
     "i'm": 20,
     'desperate': 1,
     'enough': 1,
     'read': 1,
     'android': 2,
     '@ibmbizanalytics': 1,
     'mobilefirst': 1,
     'enterprise': 1,
     'collaboration': 1,
     'online.': 1,
     'changer?': 1,
     '#doclens': 1,
     'http://t.co/fsovxciit5': 1,
     'http://t.co/qwcuhsq57u': 1,
     '@renoxalex': 3,
     'sick': 6,
     '@tacobell': 1,
     'petitioning': 1,
     'continues': 1,
     'war': 1,
     'notification': 2,
     'center': 11,
     'widgets,': 1,
     'asks': 1,
     "'drafts'": 1,
     'note': 3,
     'creation': 1,
     'http://t.co/qjgikludvh': 1,
     'im': 11,
     '#aapl:one': 1,
     'thing': 6,
     'everyone': 2,
     'getting': 9,
     'comes': 2,
     'televis...http://t.co/elxd0efhiv': 1,
     'hang': 2,
     'loose': 1,
     '???': 1,
     'facebook': 2,
     'dumbass': 1,
     'deleted': 5,
     'redownload': 1,
     'says': 7,
     'ios7': 1,
     'suck': 6,
     'ass': 10,
     'cha': 1,
     'fix': 37,
     '!!!': 2,
     'yo': 9,
     'people?': 1,
     'easier': 1,
     'contacts': 2,
     'already,': 1,
     'gosh': 1,
     'damn': 5,
     'it!!!': 1,
     'clock': 1,
     'disappear': 2,
     'siri?': 1,
     'super': 1,
     'suddenly': 1,
     'see': 1,
     'patents': 4,
     'active': 3,
     'fall': 3,
     'protection': 3,
     'system': 4,
     'shifts': 4,
     'iphones': 7,
     'midair': 3,
     'http://t.co/umvw5neojc': 1,
     "i've": 8,
     'two': 5,
     'already': 3,
     'shout': 3,
     'television': 1,
     'http://t.co/s72wxz4dcq': 1,
     'http://t.co/boch9dbt3q': 1,
     'abrick': 1,
     'stuck': 1,
     'logo': 1,
     'product': 5,
     'hunters:': 1,
     'functional': 1,
     '(and': 3,
     'whimsical)': 1,
     'keyboards': 3,
     '#ios8': 3,
     'forbes': 1,
     'http://t.co/yugbzfhsnb': 1,
     'allowing': 1,
     'ppl': 1,
     'access': 2,
     'camera': 3,
     'locked': 1,
     'beginning': 1,
     'products': 6,
     'crap': 2,
     '6th': 1,
     '#applesuport': 1,
     'wrongdoing': 1,
     'worse': 5,
     'ever': 5,
     'http://t.co/jhps71df0w': 1,
     'updates,': 1,
     'iphone,': 3,
     'ipad': 12,
     'ipod': 10,
     'touch': 3,
     'charge': 3,
     'royally': 1,
     'fucked': 5,
     '@nintendo': 1,
     '@sega.': 1,
     "they'd": 2,
     'emulation,': 1,
     'characters,': 1,
     'content/portfolios,': 1,
     'recognition,': 1,
     'developer': 1,
     'contacts.': 1,
     'group': 2,
     'chats': 1,
     'tripping': 1,
     'tired': 5,
     'bullshit': 3,
     'holding': 1,
     'responsible': 1,
     '.': 5,
     'computer': 6,
     '@mkschuster:': 1,
     '@landonboyd93': 1,
     '@mochasucks': 1,
     'penis': 1,
     'emoji?': 1,
     'implying': 1,
     'dick': 3,
     'looks': 2,
     'eggplant.': 1,
     'mini-flash': 1,
     'crash:': 1,
     'morning:': 1,
     'nothing': 5,
     'suggested': 1,
     'would': 6,
     'widely': 1,
     'held...': 1,
     'http://t.co/ihmonrcekx': 1,
     'apples': 1,
     'earbuds': 1,
     'weak': 5,
     'literally': 3,
     'cannot': 4,
     'withstand': 1,
     'damage': 1,
     'wasted': 2,
     '@microsoft': 1,
     '@stevejobs': 3,
     '@billgates': 2,
     'common': 2,
     'somebody': 1,
     'http://t.co/9z0qeibtlc': 1,
     'difficult': 3,
     'qualify': 1,
     '#geniusbar': 1,
     'appointment': 1,
     'days?': 1,
     '#unneccessary': 1,
     'dammit': 2,
     '@yungbaaz:': 1,
     'catch': 1,
     'maverick': 1,
     'wave': 1,
     'iphone?': 1,
     "didn't": 5,
     'so.': 1,
     '#surfsupsamsung': 1,
     'english': 1,
     'this?': 2,
     'mean?': 1,
     'http://t.co/pzb18o3kvj': 1,
     "ain't": 2,
     '#furstrated': 1,
     '#annoyed': 1,
     '#charging': 1,
     'yea': 4,
     '600': 4,
     'dollars': 5,
     'dies': 5,
     '30%': 4,
     '@fazenikan': 2,
     'homie': 2,
     '@ryansconcepts:': 1,
     '@fazenikan:': 3,
     'still': 17,
     'merge': 2,
     'multiple': 2,
     "apple-id's": 2,
     'http://t.co/5bnaihk58p': 1,
     '#': 1,
     'dyslexic': 1,
     'rejoice!': 1,
     "'voice": 1,
     "text'": 1,
     'past!': 1,
     'http://t.co/wjjflyzme3': 1,
     'http://t.co/cdvtujnqgu': 1,
     'http://t.co/76qwga6ml7': 1,
     '#technology': 1,
     '#fyi': 1,
     'diag': 1,
     'support': 5,
     'lot!': 1,
     "'cannot": 1,
     'connect': 1,
     'server,': 1,
     "again',": 1,
     "'ticket": 1,
     "found'": 1,
     '#disgusting': 1,
     'http://t.co/aryybxodox': 1,
     'why?': 1,
     'http://t.co/r7brjshrxk': 1,
     'computers': 1,
     'crash': 2,
     'week': 5,
     'finals?': 1,
     '@sashametro': 1,
     'iupdate': 1,
     'process': 2,
     'incensing.': 1,
     'rubbish.': 1,
     'hopefully': 1,
     'irrelevant': 1,
     'soon.': 1,
     'going': 12,
     'press': 1,
     'button!!': 1,
     'wait': 4,
     'http://t.co/eteewiijro': 1,
     "'never'": 1,
     'interpreted': 1,
     "'ask": 1,
     'annoyingly': 1,
     "soon'": 1,
     'ask': 1,
     'rated?': 1,
     'tell': 3,
     'devs': 1,
     'means': 1,
     "jobs'": 1,
     'snarky': 1,
     'testimony': 1,
     'takes': 2,
     'stage': 154,
     'class-action': 1,
     'opening': 1,
     'http://t.co/nxet3feo5q': 1,
     'butterfingers': 1,
     'mix:': 1,
     '@#applinsider:': 1,
     'http://t.co/qm52rml6c9': 1,
     "17'": 1,
     'macbook': 8,
     'pro': 5,
     'boots': 1,
     'pink': 1,
     'vertical': 1,
     'stripes,': 1,
     'gray': 1,
     'screen,': 1,
     'shutting': 1,
     'repeating...help': 1,
     'http://t.co/xz4wb3dm73': 1,
     '@jakeflem': 3,
     "we've": 1,
     'previously': 1,
     'deal': 3,
     'annoying.': 2,
     'reset': 3,
     'nvram': 1,
     'http://t.co/eoiaf3wo5f': 1,
     '@briannaurie': 1,
     "won't": 6,
     'problem': 2,
     'good,': 1,
     'might': 3,
     'logic': 2,
     'board,': 1,
     'check': 3,
     'genius': 9,
     'real': 4,
     'competition': 1,
     'http://t.co/8cygzezqpn': 1,
     '@umo_games': 1,
     'tip!': 1,
     'seemed': 1,
     'something': 5,
     'pretty': 3,
     'same.': 1,
     'lowkey,': 1,
     'trash': 5,
     'af': 4,
     'cant': 1,
     'use': 5,
     'express': 1,
     '9': 1,
     'anymore': 1,
     'irritating': 1,
     'outta': 1,
     'sincerely': 1,
     'disgruntled': 1,
     'person': 1,
     "'@_irapecouches:": 1,
     '@sydneya': 1,
     'dumb': 2,
     'upgraded': 1,
     'patent': 3,
     'screens': 2,
     'http://t.co/l2kqqhv8dp': 1,
     '@techcrunch': 2,
     '#business': 2,
     '#innovation': 2,
     'http://t.co/lvmnzpg36f': 1,
     'http://t.co/lswpdlt8ud': 1,
     '@wdtuts': 1,
     '@baxleyglass': 1,
     'belongs': 1,
     '@ang': 1,
     'third': 3,
     '@adobe': 1,
     '#employeediscount.': 1,
     'anyone': 4,
     'update': 10,
     'yosemite?': 1,
     'shit.': 3,
     'sucks,': 2,
     'cost': 1,
     'us': 5,
     'ì´å£400': 1,
     'hoping': 1,
     '@firefox': 1,
     'cave!': 1,
     'allow': 1,
     'browser': 2,
     'engines!': 1,
     '#openup': 1,
     'soon': 2,
     'come': 7,
     ...}



Replace `yourdicname` with the dictionary u have just created


```python
wordcloud = WordCloud()
wordcloud.generate_from_frequencies(frequencies=worddic)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```


![png](output_34_0.png)



```python
#alternative: remove useless words and try again.
new_worddic = worddic.copy()
remove = ['retweet','rt','fuck','fucking','anger','misplaced']
```


```python

```
