#!/usr/bin/env python

import os
import sys
import random
import subprocess
import wikipedia
from twython import Twython


ApiKey = ''
ApiSecret = ''
AccessToken = ''
AccessTokenSecret = ''
cred_file = os.path.dirname(os.path.realpath(__file__)) +'/.auth'
twitter_allowed_char = 140

def get_api_token():
    ''' Obtain Twitter app's API token from file .auth

    Returns list
    '''
    f = open(cred_file, 'rb')
    c = f.read()
    t = c.splitlines()
    return t[0:4]

def get_today_str():
    ''' Obtain current date in 'Month_Date' format, e.g., March 3

    Returns str
    '''
    d = subprocess.check_output(["date", "+%B_%d"])
    d_str = d.translate(None, '\n')
    return d_str

def get_events_list(date_str):
    ''' Obtain the list of events for date_str

    Returns list
    '''
    page = wikipedia.WikipediaPage(title=date_str)
    events = page.section("Events")
    events_list = events.splitlines()
    return events_list

def get_tweet_str():
    ''' Obtain the string to tweet. It does sanity checks.

    Returns str
    '''
    trials = 10
    today_str = get_today_str()
    tweet_str = 'Nothing to tweet today. #' + today_str
    events_list = get_events_list(today_str)
    list_size = len(events_list)
    if list_size == 0:
        return tweet_str
    
    while trials > 0:
        i = random.randrange(0, list_size)
        entry_str = events_list[i]
        if len(entry_str) + len(' #' + today_str) <= twitter_allowed_char:
            tweet_str = entry_str + ' #' + today_str
            return tweet_str
        else:
            trials = trials - 1
    
    return tweet_str


def do_tweet(str):
    ''' Tweet str to Twitter

    '''
    [ApiKey, ApiSecret, AccessToken, AccessTokenSecret] = get_api_token()
    api = Twython(ApiKey, ApiSecret, AccessToken, AccessTokenSecret)
    api.update_status(status=str)
    print "Tweeted: " + str


if __name__ == '__main__':
    tweet_str = get_tweet_str()
    do_tweet(tweet_str)


    

