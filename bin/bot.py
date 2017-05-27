import praw
import config

def login_bot():
    '''
    Returns a new instance of a reddit connection for bot.
    '''
    r = praw.Reddit(
            username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent
            )
    return r

def or_check(comment, rules):
    '''
    Returns True if comments contains one of the strings in rules, else False.
    '''
    for i in rules:
        if i in comment:
            return True
    return False
def and_check(comment, rules):
    '''
    Returns true if comment contains all parameters in rules, False otherwise.
    '''
    for i in rules:
        if i not in comment:
            return False
    return True

def run_bot(r):
    '''
    Main bot protocol, takes in reddit connection for praw as input
    '''
    counter = 0
    for comment in r.subreddit('Warhammer40k').comments(limit = 500):
        if ("emperor" in comment.body or "emperor's") and ("mankind" in comment.body or "chosen" in comment.body or "lord" in comment.body):
            comment.reply("GLORY TO OUR EMPEROR, THE HOLY SAVIOR OF MANKIND")
            comment.upvote()
    for comment in r.subreddit('40k').comments(limit = 500):
        if ("emperor" in comment.body or "emperor's") and ("mankind" in comment.body or "chosen" in comment.body or "lord" in comment.body):
            comment.reply("GLORY TO OUR EMPEROR, THE HOLY SAVIOR OF MANKIND")
            comment.upvote()
