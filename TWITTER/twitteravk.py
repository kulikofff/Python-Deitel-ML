import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key,
                           keys.consumer_secret)

auth.set_access_token(keys.access_token,
                      keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


nasa = api.get_user('nasa')
#print(nasa)
#print()
print(nasa.id, nasa.name, nasa.screen_name, nasa.description, nasa.status.text, nasa.followers_count, nasa.friends_count)
print()
#print(api.me())

#followers
followers = []
cursor = tweepy.Cursor(api.followers, screen_name='nasa')

for account in cursor.items(10):
    followers.append(account.screen_name)

print('Followers:',
      ' '.join(sorted(followers, key=lambda s: s.lower())))

#friends
friends = []
cursor = tweepy.Cursor(api.friends, screen_name='nasa')
for friend in cursor.items(10):
        friends.append(friend.screen_name)

print('Friends:',
      ' '.join(sorted(friends, key=lambda s: s.lower())))

#tweets
nasa_tweets = api.user_timeline(screen_name='nasa', count=3)
for tweet in nasa_tweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')



#print_tweets on filter
from tweetutilities import print_tweets
tweets = api.search(q='Mars Opportunity Rover', count=3)

print(print_tweets(tweets))

tweets = api.search(q='from:nasa since:2018-09-01', count=3)
print(print_tweets(tweets))

tweets = api.search(q='#collegefootball', count=2)
print(print_tweets(tweets))

#trends
#http://www.woeidlookup.com
trends_available = api.trends_available()
print(len(trends_available))
print(trends_available[0])

world_trends = api.trends_place(id=1)
print(world_trends)

trends_list = world_trends[0]['trends']
print(trends_list[0])

trends_list = [t for t in trends_list if t['tweet_volume']]
from operator import itemgetter
trends_list.sort(key=itemgetter('tweet_volume'), reverse=True)
for trend in trends_list[:5]:
    print(trend['name'])

#NYC
nyc_trends = api.trends_place(id=2459115) # WOEID Нью-Йорка
nyc_list = nyc_trends[0]['trends']
nyc_list = [t for t in nyc_list if t['tweet_volume']]
nyc_list.sort(key=itemgetter('tweet_volume'), reverse=True) 
for trend in nyc_list[:5]:
    print(trend['name'])

#vocab cloud
topics = {}
for trend in nyc_list:
    topics[trend['name']] = trend['tweet_volume']
from wordcloud import WordCloud
wordcloud = WordCloud(width=1600, height=900,
    prefer_horizontal=0.5, min_font_size=10, colormap='prism',
    background_color='white')

wordcloud = wordcloud.fit_words(topics)
wordcloud = wordcloud.to_file('TrendingTwitter.png')

#Data clearing
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.RESERVED)
tweet_text = 'RT A sample retweet with a URL https://nasa.gov'
print(p.clean(tweet_text))


#Listener
from tweetlistener import TweetListener
tweet_listener = TweetListener(api)

tweet_stream = tweepy.Stream(auth=api.auth,
                             listener=tweet_listener)
tweet_stream.filter(track=['Mars Rover'], is_async=True)