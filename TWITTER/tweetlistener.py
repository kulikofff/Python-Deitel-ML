import tweepy
from textblob import TextBlob

class TweetListener(tweepy.StreamListener):
    """Обрабатывает входной поток твитов."""
    def __init__(self, api, limit=10):
        """Создает переменные экземпляров для отслеживания количества твитов."""
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
        super().__init__(api) # вызывает версию суперкласса

    def on_connect(self):
        """Вызывается при успешной попытке подключения, чтобы вы могли
        выполнить соответствующие операции приложения в этот момент."""
        print('Connection successful\n')

    def on_status(self, status):
        """Вызывается, когда Twitter отправляет вам новый твит."""
        # Получение текста твита
        try:
            tweet_text = status.extended_tweet.full_text
        except:
            tweet_text = status.text
        print(f'Screen name: {status.user.screen_name}:')
        print(f' Language: {status.lang}')
        print(f' Status: {tweet_text}')
        if status.lang != 'en':
            print(f' Translated: {TextBlob(tweet_text).translate()}')
        print()
        self.tweet_count += 1 # Счетчик обработанных твитов
        # При достижении TWEET_LIMIT вернуть False, чтобы завершить
        # работу с потоком
        return self.tweet_count != self.TWEET_LIMIT