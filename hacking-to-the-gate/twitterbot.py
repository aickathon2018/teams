import csv
import tweepy
import pandas as pd
####input your credentials here
from tweepy.auth import OAuthHandler
auth = OAuthHandler('WNUpykrIjiGF0NKoV7qk7uiNj', 'Nhe0GjOkbaQKbPMLTqcAYQnqMnz3Edpdup28h2R2KqRLa6iBDN')
auth.set_access_token('956917059287375875-EThit80MxgQPTJlh7ZObqyHsoV8Q2D7', 'eLv893meGppqfX3xOr8SJ93kpsbZpoOiRsVM3XTgJryZM')

auth = tweepy.OAuthHandler('WNUpykrIjiGF0NKoV7qk7uiNj', 'Nhe0GjOkbaQKbPMLTqcAYQnqMnz3Edpdup28h2R2KqRLa6iBDN')
auth.set_access_token('956917059287375875-EThit80MxgQPTJlh7ZObqyHsoV8Q2D7', 'eLv893meGppqfX3xOr8SJ93kpsbZpoOiRsVM3XTgJryZM')
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('data.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#ootd",count=100,
                           include_entities=True,
                           lang="en",
                           since="2018-11-01").items():

    if 'media' in tweet.entities:
        for image in  tweet.entities['media']:
            favs = tweet.favorite_count
            if favs > 30:
                csvWriter.writerow([favs, image['media_url'], tweet.created_at])