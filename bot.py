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
    for post in r.subreddit('40k').new(limit = 25):
        for comment in post.comments:
            if "emperor" in and "mankind" comment.body:
                comment.reply("GLORY TO OUR EMPEROR, THE HOLY SAVIOR OF MANKIND")
                comment.upvote()

r = login_bot()
run_bot(r)
