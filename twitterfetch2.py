import tweepy
import pandas as pd
import csv
import time
from collections import Counter

consumer_key="x5ER0kkhEvbS8cJg8jDF2Z04T"
consumer_secret="6WSZoraAH8CIMqkijT04OkdFSQ42LvoRSp7FFPmNTKT0h26fSR"

access_token="1224316478218014722-pUGe6PQPmiN8lzzwJc4Kmb2XGnxudh"
access_token_secret="BcLOFyeR6ewEuHWfelAjqtIGS64tH5zZxT9EHx5EDjJ8d"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets(query):
    tweets = []
    ids = []
    results = tweepy.Cursor(api.search, q=query+'-filter:retweets', lang='fr').items(300)
    while len(ids) < 100:
        for status in results:
            id = status.user.id
            ids.append(id)
            print(len(ids))
            print(ids)
    
    for id in ids:
        statuses = tweepy.Cursor(api.user_timeline, user_id=id, tweet_mode='extended', include_rts=False).items(20)
        for status in statuses:
            tweet = status.full_text
            tweets.append(tweet)
    return tweets

TXTtweets = fetch_tweets('TXT')


