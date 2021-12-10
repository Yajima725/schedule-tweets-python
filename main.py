import tweepy
import sched
import time
import datetime

# API Keys
CK = "Consumer Key"
CS = "Consumer Secret"
AT = "Access Token"
AS = "Access Secret"

def tweet(text):
    """tweet"""
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)
    api.update_status(text)

def tweet_sched(post_date, tweet_text):
    """Setting the time"""
    scheduler = sched.scheduler(time.time, time.sleep)
    run_at = int(time.mktime(post_date.utctimetuple()))
    scheduler.enterabs(run_at, 1, tweet, (tweet_text,))
    scheduler.run()


#Example
post_date = datetime.datetime(2021, 12, 9, 17, 0)
tweet_text = "test"
tweet_sched(post_date, tweet_text)
