import tweepy
import datetime

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="mtWTFss"
consumer_secret="mtWTFss"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="mtWTFss"
access_token_secret="mtWTFss"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
page = 1
stop_loop = False
while not stop_loop:
    tweets = api.user_timeline(username, page=page)
    if not tweets:
        break
    for tweet in tweets:
        if datetime.date(YEAR, MONTH, DAY) < tweet.created_at:
            stop_loop = True
            break
        # Do the tweet process here
    page+=1
    time.sleep(500)
