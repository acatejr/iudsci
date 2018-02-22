# Example 9
# Exceptions
# In this example, delete some part of the access token.
# This will raise an exception with code 89

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

try:
    public_tweets = api.home_timeline(count="2")
    for tweet in public_tweets:
        print(tweet.text)
except tweepy.TweepError as err:
    print(err)
    print(err.args[0][0]['code'])
    print(err.args[0][0]['message'])

# Following is a small snippet to handle rate-limit errors.

# def limit_handled(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             time.sleep(15 * 60)

# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     if follower.friends_count < 300:
#         print follower.screen_name
