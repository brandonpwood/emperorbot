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


def run_bot(r):
    '''
    Main bot protocol, takes in reddit connection for praw as input
    '''
    for comment in r.subreddit('Warhammer40k').comments(limit = 400):
        if "emperor" in comment.body and (comment.author.name != "GLORYTOTHEEMPERORBOT"):
            comment.refresh()
            for rep in comment.replies:
                check = True
                if "GLORY TO THE EMPEROR, THE HOLY SAVIOR OF MANKIND" in rep.body:
                    check = False
                    break
            if check:
                comment.reply("GLORY TO THE EMPEROR, THE HOLY SAVIOR OF MANKIND")
                comment.upvote()
                print("New Comment")
                print('-------------------')
            else:
                print("Already seen this one")
                print('-------------------')
run_bot(login_bot())
