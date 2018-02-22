# Example 2
# model class
# dir() returns a list of all attributes and functions associated with the object

import tweepy
from pprint import pprint

# paste you consumer keys and access tokens here
consumer_key = "7IRyachsHv2zJjn4Ht8A6SA3K"
consumer_secret = "4jPg61HfJgf3ZDCUc7DKAe82CR1PG9fzgwzt30OL0JipX11dgO"
access_token = "17156455-7ZpOFVRiUmbpGYB164CU9Y9XK2WTdCngMkI6NK1ji"
access_token_secret = "D8fU6jV9q4E42RZWOKpOdKJEk2DWQOE7lt2qK4Ub3lORi"

# Creating an OAuthHandler Object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creating an API handle (object)
# This object is used to access all the API methods
api = tweepy.API(auth)

public_tweets = api.home_timeline(count="2")
tweet = public_tweets[0]

print(dir(tweet))

print('\n', '-'*60, '\n')

# tweet._json returns the JSON object of the tweet
pprint(tweet._json)
