#!/usr/bin/env python
'''
Tweet today-in-history event obtained from Wikipedia
'''

import os
import random
import re
import subprocess
from datetime import datetime
import wikipedia
import tweepy
from bs4 import BeautifulSoup


CRED_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '.auth')
TWITTER_ALLOWED_CHAR = 260


def get_app_credential():
    ''' Obtain Twitter app's credential from envirnoment or file .auth

    If any of environment variables TIH_API_KEY, TIH_API_SECRET,
    TIH_ACCESS_TOKEN, TIH_ACCESS_TOKEN_SECRET exist, they override the
    corresponding secret values in file .auth

    Returns list
    '''
    api_key = os.environ.get('TIH_API_KEY')
    api_secret = os.environ.get('TIH_API_SECRET')
    access_token = os.environ.get('TIH_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TIH_ACCESS_TOKEN_SECRET')
    credential = [api_key, api_secret, access_token, access_token_secret]

    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, 'r', encoding='utf-8') as fil:
            content = fil.read()
            templ = content.splitlines()
            if len(templ) < 4:
                raise Exception(CRED_FILE
                                + " is malformed. "
                                + "It needs to contain at least 4 secrets")
            return [fil if env is None else env
                    for env, fil in zip(credential, templ)]

    return credential


def get_today_str():
    ''' Obtain current date in 'Month_Date' format, e.g., March 3

    Returns str
    '''
    date_str = subprocess.check_output(["date", "+%B_%d"]).strip()
    return date_str.decode('utf-8')


def get_events_list(date_str):
    ''' Obtain the list of events for date_str

    Returns list
    '''
    content = wikipedia.WikipediaPage(title=str(date_str)).html()
    content = BeautifulSoup(content, 'html.parser').get_text()
    # Split the content into lines, dropping empty lines
    lines = [line for line in content.splitlines() if line.strip()]
    # Use some heuristics to take into account of recent wikipedia page format
    # changes in July 2024
    maybe_events = [lines[i] for i in
        range(lines.index('Events[edit]'), lines.index('Births[edit]'))]
    # Remove section headers
    events = [line for line in maybe_events if not line.endswith('[edit]')]
    # Remove braced references from end of event string
    events_trimmed = [re.sub(r'\[\d+\]', '', event) for event in events]
    return events_trimmed


def get_tweet_str():
    ''' Obtain the string to tweet. It does sanity checks.

    Returns str
    '''
    trials = 10
    today_str = get_today_str()
    tweet_str = 'Nothing to tweet today. #' + today_str
    events_list = get_events_list(today_str)
    # For debugging
    print(events_list)
    list_size = len(events_list)
    if list_size == 0:
        return tweet_str

    # Use system time as random seed
    random.seed(datetime.now().timestamp())
    while trials > 0:
        i = random.randrange(0, list_size)
        entry_str = events_list[i]
        if len(entry_str) + len(' #' + today_str) <= TWITTER_ALLOWED_CHAR:
            tweet_str = entry_str + ' #' + today_str
            break

        trials = trials - 1

    return tweet_str


def do_tweet(tweet_str):
    ''' Tweet twt_str to Twitter

    '''
    [apikey, apisecret, accesstoken, accesstokensecret] = get_app_credential()
    client = tweepy.Client(consumer_key=apikey,
                           consumer_secret=apisecret,
                           access_token=accesstoken,
                           access_token_secret=accesstokensecret)
    response = client.create_tweet(text=tweet_str)
    print("Tweeted: ", tweet_str)
    print(response)


if __name__ == '__main__':
    TWT_STR = get_tweet_str()
    print(TWT_STR)
    # Set environment variable TIH_DRYRUN to any non-empty value to skip tweet
    # publication
    if not os.environ.get('TIH_DRYRUN'):
        do_tweet(TWT_STR)
