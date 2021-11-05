import tweepy
import json
from datetime import date

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = "mtWTFss"
consumer_secret = "mtWTFss"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = "mtWTFss"
access_token_secret = "mtWTFss"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.verify_credentials().name)


class Listener(tweepy.Stream):
    tweet_counter = 0
    stop_at = 1000

    def on_data(self, data):
        Listener.tweet_counter += 1
        if(Listener.tweet_counter < Listener.stop_at):
            print(str(Listener.tweet_counter))
            tweet = json.loads(data)
            for key in tweet:
                print(key, ":", tweet[key])
            return True
        else:
            print("Either Max number reached or time limit up at:"
                  + str(Listener.tweet_counter) + " outputs")
            self.disconnect()
            return False


stream = Listener(consumer_key, consumer_secret, access_token, access_token_secret)

# Atlanta area.
stream.filter(track=["Kshchablo", "Shchablo"])
