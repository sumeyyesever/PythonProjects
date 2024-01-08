from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "python.sumeyye@gmail.com"
TWITTER_PASSWORD = os.environ["MY_PASSWORD"]

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_to_provider(TWITTER_EMAIL, TWITTER_PASSWORD, promised_up=PROMISED_UP, promised_down=PROMISED_DOWN)
