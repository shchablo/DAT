from tweepy import (Stream, OAuthHandler)
from tweepy.streaming import StreamListener

class Listener(Stream):

    tweet_counter = 0 # Static variable

    def login(self):
        CONSUMER_KEY = "mtWTFss"
        CONSUMER_SECRET = "mtWTFss"
        ACCESS_TOKEN = "mtWTFss"
        ACCESS_TOKEN_SECRET = "mtWTFss"

        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

    def __init__(self, time_limit=8):
        self.start_time = time.time()
        self.limit = time_limit
        super(Listener, self).__init__()

    def on_data(self, data):
        Listener.tweet_counter += 1
        if (time.time() - self.start_time) < self.limit and Listener.tweet_counter < Listener.stop_at:
            print(str(Listener.tweet_counter)+data)
            return True
        else:
            print("Either Max number reached or time limit up at:"+ str(Listener.tweet_counter)+" outputs")
            self.saveFile.close()
            return False

    #def on_status(self, status):
        #Listener.tweet_counter += 1
        #print(str(Listener.tweet_counter) + '. Screen name = "%s" Tweet = "%s"'
              #%(status.author.screen_name, status.text.replace('\n', ' ')))

        #if Listener.tweet_counter < Listener.stop_at and (time.time() - self.start_time) < self.limit:
            #return True

        #else:
            #print('Max num reached or time elapsed= ' + str(Listener.tweet_counter))
            #return False

    def getTweetsByGPS(self, stop_at_number, latitude_start, longitude_start, latitude_finish, longitude_finish):
        try:
            Listener.stop_at = stop_at_number # Create static variable
            auth = self.login()
            streaming_api = Stream(auth, Listener(), timeout=60) # Socket timeout value
            streaming_api.filter(follow=None, locations=[latitude_start, longitude_start, latitude_finish, longitude_finish])
        except KeyboardInterrupt:
            print('Got keyboard interrupt')

    def getTweetsByHashtag(self, stop_at_number, hashtag):
        try:
            Listener.stop_at = stop_at_number
            auth = self.login()
            streaming_api = Stream(auth, Listener(), timeout=60)
            # Atlanta area.
            streaming_api.filter(track=[hashtag])
        except KeyboardInterrupt:
            print('Got keyboard interrupt')


    listener = Listener()
    #listener.getTweetsByGPS(20, -84.395198, 33.746876, -84.385585, 33.841601) # Atlanta area.
    listener.getTweetsByHashtag(1000,"hi")
