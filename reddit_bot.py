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
# Comment
def run_robot(r):
    for comment in r.subreddit('CosmicJaxTest').comments(limit=10):
        if 'Hi' in comment.body:
            print('Found comment')
            comment.reply('Hello there!')
    time.sleep(10)

def get_completed():
    with open('completed.txt', 'r') as file:
        completed = file.read()
        completed = completed.split('\n')
    return completed

r = bot_login()
# List of titles posted by the bot
completed = get_completed()

# Make a post
def bot_post(r, title, content):
    if title not in completed:
        r.subreddit('CosmicJaxTest').submit(title, selftext=content, spoiler=True)
        with open('completed.txt', 'a') as file:
            file.write(title + '\n')
    time.sleep(3600)


#while True:
    #run_robot(r)
#bot_post(r)