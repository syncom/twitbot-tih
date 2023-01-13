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
   <http://www.instructables.com/id/Raspberry-Pi-Twitterbot/?ALLSTEPS>.

3. Set up authentication and authorization secrets. The preferred way is to set
   environment variables `TIH_APP_KEY`, `TIH_APP_SECRET`, `TIH_OAUTH_TOKEN`,
   and `TIH_OAUTH_TOKEN_SECRET` with API Key, API Secret, Access Token, and
   Access Token Secret values obtained in the last step. Alternatively, one can
   override the corresponding strings in the file [.auth](./.auth) with
   appropriate secret strings. When any of the aformetioned environment
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
