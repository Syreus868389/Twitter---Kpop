import tweepy
import pandas as pd
import csv
import time

consumer_key="x5ER0kkhEvbS8cJg8jDF2Z04T"
consumer_secret="6WSZoraAH8CIMqkijT04OkdFSQ42LvoRSp7FFPmNTKT0h26fSR"

access_token="1224316478218014722-pUGe6PQPmiN8lzzwJc4Kmb2XGnxudh"
access_token_secret="BcLOFyeR6ewEuHWfelAjqtIGS64tH5zZxT9EHx5EDjJ8d"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

results = tweepy.Cursor(api.search, q='TXT', tweet_mode='extended')
print(results)

def fetch_tweets(query):
    tweets = []
    ids = []
    results = tweepy.Cursor(api.search, q=query, tweet_mode='extended').items()
    print(results)
    while len(ids) < 100:
        for status in results:
            id = status.user_id
            ids.append(id)
    for id in ids:
        statuses = tweepy.Cursor(api.user_timeline, user_id=id).items()
        tweet = statuses.full_text
        tweets.append(tweet)
    return tweets


