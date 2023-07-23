# twitbot-tih

[![Shellcheck](https://github.com/syncom/twitbot-tih/actions/workflows/shellcheck.yml/badge.svg)](https://github.com/syncom/twitbot-tih/actions/workflows/shellcheck.yml)
[![Pylint](https://github.com/syncom/twitbot-tih/actions/workflows/pylint.yml/badge.svg)](https://github.com/syncom/twitbot-tih/actions/workflows/pylint.yml)

A Twitter bot that tweets today-in-history events.

## Dependencies

- Python 3 with virtual environment. On Ubuntu, install `python3-virtualenv`.

- Unix/Linux environment and the 'date' command

- If you run on a Raspberry Pi, you might need to install `rng-tools` for the
  SSL connection to work

## Usage

1. Install with the following commands

   ```bash
   git clone https://github.com/syncom/twitbot-tih.git
   cd twitbot-tih
   make install
   ```

2. Create a Twitter app and obtain the API Key, API Secret, Access Token, and
   Access Token Secret for the app. This can be done by following the
   instructions at:
   <https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api>.
   After April 2023, if you start seeing API authentication errors, and a
   message like "This app has violated Twitter rules and policies" on the
   Twitter app setting page, sign up for the Free tier of "[Twitter API
   v2](https://developer.twitter.com/en/portal/products)" (at no cost), and
   clicked button "downgrade to free"; this resolved the auth issue
   ([reference](https://twittercommunity.com/t/this-app-has-violated-twitter-rules-and-policies/191204/10)).
   You may also need to put the Twitter app under a "project" for better
   organization and monitoring of the app.

3. Set up authentication and authorization secrets. The preferred way is to set
   environment variables `TIH_API_KEY`, `TIH_API_SECRET`, `TIH_ACCESS_TOKEN`,
   and `TIH_ACCESS_TOKEN_SECRET` with API Key, API Secret, Access Token, and
   Access Token Secret values obtained in the last step. Alternatively, one can
   override the corresponding strings in the file [.auth](./.auth) with
   appropriate secret strings. When any of the aforementioned environment
   variables are set, they take precedence over values in the `.auth` file.

4. Activate the virtual environment.

   ```bash
   . ./venv
   ```

5. In virtual environment, run `python today_in_history_bot.py` to tweet.

6. (Optional) Create a cron job to invoke the bot once a day.
   [twitbot-tih-run.sh](twitbot-tih-run.sh) shows an example script that can be
   called within the cronjob.

7. To uninstall, `deactivate` from the virtual environment if needed, and do
   `make clean`.
