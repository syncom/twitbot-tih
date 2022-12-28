# twitbot-tih

[![Shellcheck](https://github.com/syncom/twitbot-tih/actions/workflows/shellcheck.yml/badge.svg)](https://github.com/syncom/twitbot-tih/actions/workflows/shellcheck.yml)
[![Pylint](https://github.com/syncom/twitbot-tih/actions/workflows/pylint.yml/badge.svg)](https://github.com/syncom/twitbot-tih/actions/workflows/pylint.yml)

A Twitter bot that tweets today-in-history events

## Dependencies

- Python 3, and modules:

  wikipedia,
  twython,
  pyOpenSSL,
  ndg-httpsclient,
  pyasn1

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

2. Create a Twitter app and obtain the API Key, API Secret, Access
Token, and Access Token Secret for the app. This can be done by
following the instructions at:
http://www.instructables.com/id/Raspberry-Pi-Twitterbot/?ALLSTEPS.

3. Override the corresponding strings in the file '.auth' with
appropriate Twitter app API access token strings obtained in the last
step.

4. Activate the virtual environment.

    ```bash
    . ./venv
    ```

5. In virtual environment, run 'python today_in_history_bot.py' to tweet.

6. (Optional) Create a cron job to invoke the bot once a day.
[twitbot-tih-run.sh](twitbot-tih-run.sh) shows an example script that can be
called within the cronjob.

7. To uninstall, `deactivate` from the virtual environment if needed, and do
`make clean`.
