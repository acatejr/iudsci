import csv
import tweepy
import os
import time
from config import *

""" The tweets collected would be stored as a CSV file "tweets.csv" 
with the following contents: id, lang, user.screen_name, text.
"""
# Helper functions
# The rate-limit function
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:        
            print("Rate limit exceeded.  Waiting 15 minutes.")
            time.sleep(15 * 60)

# ------------------------------------------------------------------------
# Main Program
# ------------------------------------------------------------------------

# Imported from config.py
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# create api object after proper authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_tag = "#happy" 
fname = "tweets.csv"

# creating a search cursor
search_cursor = tweepy.Cursor(api.search, search_tag)

# defining the field names
field_names = ['ID', 'Language', 'Screen Name', 'Text']
    
with open(fname, 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow([fn for fn in field_names])
    for t in limit_handled(search_cursor.items()):
        tweet = t._json
        id = tweet['id']
        lang = tweet['lang']
        user_screen_name = tweet['user']['screen_name']
        text = tweet['text'].encode('utf-8')
        csv_writer.writerow([id, lang, user_screen_name, text])
