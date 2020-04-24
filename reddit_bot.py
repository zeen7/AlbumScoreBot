import praw
from config import username, password, client_id, client_secret
import time


def bot_login():
    r=praw.Reddit(username=username,
    password=password,
    client_id=client_id,
    client_secret=client_secret,
    user_agent="ZeN's NBA News Reddit Bot v0.1")
    return r
def run_robot(r):
    for comment in r.subreddit('CosmicJaxTest').comments(limit=10):
        if 'Hi' in comment.body:
            print('Found comment')
            comment.reply('Hello there!')
    time.sleep(10)
def bot_post(r):
    title = 'Test'
    r.subreddit('CosmicJaxTest').submit(title, selftext="Test")


r=bot_login()
#while True:
    #run_robot(r)
bot_post(r)