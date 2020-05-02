# Methods that comment and post on Reddit
import praw
from config import username, password, client_id, client_secret
import time
import os

subreddit = ''

def bot_login():
    r=praw.Reddit(username=username,
    password=password,
    client_id=client_id,
    client_secret=client_secret,
    user_agent="FantanoScoreBot")
    return r

# Reply with the comment "Hello there!" if someone posts the comment "Hi"
# def comment_bot(r):
#     for comment in r.subreddit(subreddit).comments(limit=10):
#         if 'Hi' in comment.body:
#             print('Found comment')
#             comment.reply('Hello there!')
#     time.sleep(10)

# Reads the file completed.txt to check if this post has already been posted
def get_completed():
    with open('completed.txt', 'r') as file:
        completed = file.read()
        completed = completed.split('\n')
    return completed

r = bot_login()


# Make a post
def bot_post(r, title, content):
    # List of titles posted by the bot
    completed = get_completed()
    if title not in completed:
        r.subreddit(subreddit).submit(title, selftext=content, spoiler=True)
        os.remove('completed.txt')
        with open('completed.txt', 'a') as file:
            file.write(title)
    # Sleeps for 1 hour after bot_post is ran
    # time.sleep(3600)


#while True:
    #run_robot(r)
#bot_post(r)