from InstaFollower import InstaFollower
import os

SIMILAR_ACCOUNT = input("Enter the accounts username here: ")
USERNAME = "python.sumeyye@gmail.com"
PASSWORD = os.environ["MY_PASSWORD"]

insta_bot = InstaFollower()
insta_bot.login(USERNAME, PASSWORD)
insta_bot.find_followers(SIMILAR_ACCOUNT)
insta_bot.follow()
