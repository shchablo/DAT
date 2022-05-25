# -*- coding: utf-8 -*-
import tweepy as tw
import re
import csv
from pathlib import Path

from alive_progress import alive_bar

from datetime import datetime
from datetime import timedelta


def dump(path2data, numTweets = 35, behindDays = 1):

    CONSUMER_KEY = "TYqqaZVwDdyb3Oln96yx7TQ4C"
    CONSUMER_SECRET = "DGC9f5qU0SQIV97HV9t0PMZ7rSTjwt683YZy8hEiqINkCxrcbS"
    OAUTH_TOKEN = "1451462722063900673-jnxer3JNqepS8NpN3SbTvJSfDffySc"
    OAUTH_TOKEN_SECRET = "XhEBJVHqisWvcXJoU9TPrhyC25ZBE3ThKp2ETrtjEpWOQ"

    NUMBER_of_TWEETS = numTweets
    SEARCH_BEHIND_DAYS= behindDays

    today_date=datetime.today().strftime('%Y-%m-%d')
    today_date_datef = datetime.strptime(today_date, '%Y-%m-%d')
    start_date = (today_date_datef + timedelta(days=SEARCH_BEHIND_DAYS)).date()

    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2


    import http.client
    import urllib.parse as urlparse

    def unshortenurl(url):
        parsed = urlparse.urlparse(url)
        h = http.client.HTTPConnection(parsed.netloc)
        h.request('HEAD', parsed.path)
        response = h.getresponse()
        if response.status >= 300 and response.status < 400 and response.getheader('Location'):
            return response.getheader('Location')
        else: return url

    auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)

    search_terms=["#NFT -filter:retweets"]

    def extract_hash_tags(s):
        return set(part[1:] for part in s.split() if part.startswith('#'))

    tweets = tw.Cursor(api.search_tweets, q=search_terms, lang="en",
                   until=start_date).items(NUMBER_of_TWEETS)

    data_folder = Path(path2data)
    with open(data_folder, 'a', encoding="utf8", newline='' ) as csvfile:
        fieldnames = ['Keywords', 'URLs', 'Hashtags', 'User Name', 'Screen Name',
                      'Tweet Created at', 'Tweet Text', 'Location',
                      'Likes', 'Retweets']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        with alive_bar(NUMBER_of_TWEETS, bar = 'classic2', spinner = 'classic') as bar:
            for tweet in tweets:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
                hashtags = set(part[1:] for part in  tweet.text.split() if part.startswith('#'))
                dict_ = {
                         'Keywords': search_terms,
                         'URLs': urls,
                         'Hashtags': hashtags,
                         'User Name': tweet.user.name,
                         'Screen Name': tweet.user.screen_name,
                         'Tweet Created at': tweet.created_at,
                         'Tweet Text': tweet.text,
                         'Location': tweet.user.location,
                         'Likes': tweet.favorite_count,
                         'Retweets': tweet.retweet_count
                         }
                writer.writerow(dict_)
                bar()
