import tweepy

consumer_key="x5ER0kkhEvbS8cJg8jDF2Z04T"
consumer_secret="6WSZoraAH8CIMqkijT04OkdFSQ42LvoRSp7FFPmNTKT0h26fSR"

access_token="1224316478218014722-pUGe6PQPmiN8lzzwJc4Kmb2XGnxudh"
access_token_secret="BcLOFyeR6ewEuHWfelAjqtIGS64tH5zZxT9EHx5EDjJ8d"

dog = "oui"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.me().name)