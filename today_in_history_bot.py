#!/usr/bin/env python
'''
Tweet today-in-history event obtained from Wikipedia
'''

import os
import random
import subprocess
from datetime import datetime
import wikipedia
from twython import Twython


CRED_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '.auth')
TWITTER_ALLOWED_CHAR = 260


def get_api_token():
    ''' Obtain Twitter app's API token values from envirnoment or file .auth.
    If any of environment variables TIH_APP_KEY, TIH_APP_SECRET,
    TIH_OAUTH_TOKEN, TIH_OAUTH_TOKEN_SECRET exist, they override the
    corresponding secret values in file .auth.

    Returns list
    '''
    app_key = os.environ.get('TIH_APP_KEY')
    app_secret = os.environ.get('TIH_APP_SECRET')
    oauth_token = os.environ.get('TIH_OAUTH_TOKEN')
    oauth_token_secret = os.environ.get('TIH_OAUTH_TOKEN_SECRET')
    credential = [app_key, app_secret, oauth_token, oauth_token_secret]

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
    page = wikipedia.WikipediaPage(title=str(date_str))
    # Use some heuristics to take into account of recent wikipedia page format
    # changes
    maybe_events = [page.section(page.sections[i]) for i in
                    range(page.sections.index('Events'),
                          page.sections.index('Births'))]
    # Drop empty string
    events = '\n'.join([e.strip() for e in maybe_events if e.strip()])
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
    [apikey, apisecret, accesstoken, accesstokensecret] = get_api_token()
    api = Twython(apikey, apisecret, accesstoken, accesstokensecret)
    api.update_status(status=tweet_str)
    print("Tweeted: ", tweet_str)


if __name__ == '__main__':
    TWT_STR = get_tweet_str()
    print(TWT_STR)
    # Set environment variable TIH_DRYRUN to any non-empty value to skip tweet
    # publication
    if not os.environ.get('TIH_DRYRUN'):
        do_tweet(TWT_STR)
