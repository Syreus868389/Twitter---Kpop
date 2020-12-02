import tweepy
import pandas as pd
import csv
import time
from os import path, getcwd
from collections import Counter
from nltk.corpus import stopwords
import numpy as np
from PIL import Image 
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = set(stopwords.words('french'))
mots_stop = ['les','à','a']


d = getcwd()
image = Image.open(path.join(d, "Twitter-Logo.png"))
mask = np.array(image)

consumer_key="x5ER0kkhEvbS8cJg8jDF2Z04T"
consumer_secret="6WSZoraAH8CIMqkijT04OkdFSQ42LvoRSp7FFPmNTKT0h26fSR"

access_token="1224316478218014722-pUGe6PQPmiN8lzzwJc4Kmb2XGnxudh"
access_token_secret="BcLOFyeR6ewEuHWfelAjqtIGS64tH5zZxT9EHx5EDjJ8d"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def get_tweet_frequency(query):
    ids = []
    tweet_corpus = []
    results = tweepy.Cursor(api.search, q=query+'-filter:retweets', lang='fr').items(300)
    for status in results:
        id = status.user.id
        ids.append(id)
        if len(ids) < 100:
            continue
        else:
            break
    
    for id in ids:
        statuses = tweepy.Cursor(api.user_timeline, user_id=id, tweet_mode='extended', include_rts=False).items(20)
        for status in statuses:
            tweet = status.full_text
            tweet_words = tweet.split(" ")
            for word in tweet_words:
                if word not in stop_words and word not in mots_stop:
                    tweet_corpus.append(word)
    tweet_count = Counter(tweet_corpus)
    
    df = pd.DataFrame(list(tweet_count.items()),columns=['Tweets','Count'])
    sorted_df = df.sort_values(by='Count', ascending=False)
    sorted_df.to_excel(query + '.xlsx')
    
    delete_keys = []
    for key,value in tweet_count.items():
        if value < 15:
           delete_keys.append(key)
        else:
            continue
    for key in delete_keys:
        tweet_count.pop(key)
    
    wordcloud = WordCloud(background_color="white", max_words=200, mask=mask).generate_from_frequencies(tweet_count)
    plt.imshow(wordcloud, interpolation="nearest")
    plt.axis("off")
    plt.savefig(query + '.png', transparent=True)
    
artist_list = ['TXT','NCT U','MAMAMOO','Stray Kids','EVERGLOW','ITZY','Smino','Damso','Naza','Charli XCX','Oh Wonder','KAYTRANADA']
    
for artist in artist_list:
    get_tweet_frequency(artist)
            







