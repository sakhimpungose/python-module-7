import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'ZxVCHYVSm8ycYrnl05G0AUw5E'
consumer_secret = '4eQRmJvMJffwqXT1wfczUiiSd0VGlLghUw0DsPj5VNEgnzYsZ5'
access_token = '1161869059-y52i0KTm43cDyTipeXM9Oc4323rpHBWB8EzHUbl'
access_secret = 'pCicr46kTrTHpQHbhXyMT8gYjFtxq6v5YZhzB0oDxidd6'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


def word_count(text, exclude = []):
    counts = {}
    
    text = text.lower()
    
    words = re.split(r'\s+|[^a-zA-Z0-9-@#]', text)

    for word in words:
        if len(word) == 0:
            continue
        if len(word) < 2 and word not in 'ai':
            continue
        elif word in exclude:
            continue
            
            
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def grow(n):
    return n * 500


df = pd.read_json('tweets.json')

words_dict = {}

for tweet in df['text']:
    results = word_count(tweet)
    
    for word in results:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
            
words = list(words_dict)
words_count = list(words_dict.values())

n = len(words)
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = list(map(grow, words_count))

plt.figure(figsize=(18,9))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Words Bubbles')

for i, txt in enumerate(words):
    plt.annotate(txt, (x[i], y[i]))    

plt.show()
