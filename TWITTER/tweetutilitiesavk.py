from geopy import OpenMapQuest
import keys
from textblob import TextBlob 
import time 
import tweepy

def print_tweets(tweets):
    for tweet in tweets:
        print(f'{tweet.screen_name}:', end=' ')
        if 'en' in tweet.lang:
            print(f'{tweet.text}\n')
        elif 'und' not in tweet.lang: # Сначала переводится на английский
            print(f'\n ORIGINAL: {tweet.text}')
            print(f'TRANSLATED: {TextBlob(tweet.text).translate()}\n')