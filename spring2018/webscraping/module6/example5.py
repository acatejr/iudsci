# Example 5
# API.followers(screen_name)
# Returns the list of the followers of the given user

import tweepy

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

screen_name = ''
followers_list = api.followers(screen_name)

for follower in followers_list:
    print(follower)
