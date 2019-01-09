#!/usr/bin/env python
# coding: utf-8

# In[1]:


# For harvesting twitter
from twitter import *

# For data visualisation
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


# In[2]:


hastag = "#BigData"

consumer_key = 'tlOGNKHjOHYuQ2ZYXOJtdBWit'
consumer_secret = 'siwK4cP3UpdV2DImLZmGWMnxxzW8ye0KmUKJtTECr2zZlZdp1G'
access_token = '860209219135565826-EOAP7QfjtXdmd1xejlKjYvArj39LFfV'
access_token_secret = 'KNGJMjOLOb0Kd5SOTuvqkt4sBQSHLxNFUHb7q7M1xSxl2'


# In[3]:


t = Twitter(auth=OAuth(access_token, access_token_secret,consumer_key, consumer_secret ))


# In[4]:


pythonTweets = t.search.tweets(q=hastag, lang='en', count = 200)


# In[5]:


#pprint(pythonTweets)
textOfMessages = [tweet['text'] for tweet in pythonTweets['statuses']]
retweetsOfTweet = [tweet['retweet_count'] for tweet in pythonTweets['statuses']]
timeCreatedAt = [tweet['created_at'] for tweet in pythonTweets['statuses']]


# In[6]:


textOfMessages


# In[7]:


# pythonTweets['statuses']


# In[8]:


print(retweetsOfTweet)
print(len(retweetsOfTweet))


# In[9]:


# timeCreatedAt


# In[10]:



# STEP 5
ENGLISH_STOP_WORDS = ["a", "about", "above", "across", "after", "afterwards",
"again", "against",
    "all", "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
    "around", "as", "at", "back", "be", "became", "because", "become",
    "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
    "below", "beside", "besides", "between", "beyond", "bill", "both",
    "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
    "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
    "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
    "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
    "find", "fire", "first", "five", "for", "former", "formerly", "forty",
    "found", "four", "from", "front", "full", "further", "get", "give", "go",
    "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
    "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
    "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
    "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
    "latterly", "least", "less", "ltd", "made", "many", "may", "me",
    "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
    "move", "much", "must", "my", "myself", "name", "namely", "neither",
    "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
    "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
    "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
    "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "same", "see", "seem", "seemed",
    "seeming", "seems", "serious", "several", "she", "should", "show", "side",
    "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
    "something", "sometime", "sometimes", "somewhere", "still", "such",
    "system", "take", "ten", "than", "that", "the", "their", "them",
    "themselves", "then", "thence", "there", "thereafter", "thereby",
    "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
    "third", "this", "those", "though", "three", "through", "throughout",
    "thru", "thus", "to", "together", "too", "top", "toward", "towards",
    "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
    "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
    "whence", "whenever", "where", "whereafter", "whereas", "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
    "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself",
    "yourselves","ago","reuters","news", ]


# In[11]:


data = np.array([timeCreatedAt, retweetsOfTweet])

df = pd.DataFrame(data=data.T, columns=('time', 'retweet'))


# In[12]:


df['retweet'] = df['retweet'].astype(int)
df = df.sort_values(by='retweet', ascending=False)
df['time'] = pd.to_datetime(df['time'])


# In[13]:


df.plot(x='time', y='retweet', figsize=(20,10), title='Timestamp of retweet')


# In[59]:


textOfMessages[0].split()


# In[101]:


lenOfText = len(textOfMessages) - 1

x=0
out = []
for x in textOfMessages:
    slicedText = x.split()
    out.extend(slicedText)


# In[ ]:





# In[94]:


from collections import Counter
page_word_freq = Counter(out).most_common()
print(len(page_word_freq), page_word_freq[:10])


# In[99]:


page_word_freq
page_word_freq_dict = dict(page_word_freq)
page_word_freq_dict


# In[100]:


get_ipython().magic('pylab inline')
from os import path
wordcloud = WordCloud(max_words=100).fit_words(page_word_freq_dict)
plt.imshow(wordcloud)
plt.axis("off")


# In[ ]:




