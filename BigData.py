#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pprint import pprint
from twitter import *


# In[3]:


consumer_key = 'tlOGNKHjOHYuQ2ZYXOJtdBWit'
consumer_secret = 'siwK4cP3UpdV2DImLZmGWMnxxzW8ye0KmUKJtTECr2zZlZdp1G'
access_token = '860209219135565826-EOAP7QfjtXdmd1xejlKjYvArj39LFfV'
access_token_secret = 'KNGJMjOLOb0Kd5SOTuvqkt4sBQSHLxNFUHb7q7M1xSxl2'


# In[4]:


t = Twitter(auth=OAuth(access_token, access_token_secret,consumer_key, consumer_secret ))


# In[5]:


pythonTweets = t.search.tweets(q="#BigData")


# In[8]:


#pprint(pythonTweets)
textOfMessages = [tweet['text'] for tweet in pythonTweets['statuses']]


# In[9]:


print(textOfMessages)


# In[7]:


pythonTweets['statuses']


# In[ ]:





# In[ ]:




