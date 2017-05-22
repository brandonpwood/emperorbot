import praw
import config

def login_bot():
    r = praw.Reddit(
            username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent
            )
    return r

def run_bot(r):
    counter = 0
    for comment in r.subreddit('40k').comments(limit = 250):
        if ("emperor" in comment.body or "emperor's") and ("mankind" in comment.body or "chosen" in comment.body or "lord" in comment.body):
            comment.reply("GLORY TO OUR EMPEROR, THE HOLY SAVIOR OF MANKIND")
            comment.upvote()

r = login_bot()
run_bot(r)
