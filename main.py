import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "dudelookbehindu's dog comment responder v0.1" )
    return r

def run_bot(r):
    for comment in r.subreddit('test').comments(limit = 25):
        if "dog" in comment.body:
            print ("String found!")
            comment.reply("I love dogs!")

r = bot_login()
run_bot(r)