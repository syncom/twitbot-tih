# twitbot-tih
A Twitter bot that tweets today-in-history events

# Dependencies

- Python 2.7, and modules: 
  	wikipedia, 
  	twython, 
  	pyOpenSSL, 
  	ndg-httpsclient, 
  	pyasn1


- Unix/Linux environment and the 'date' command

# Usage

1. Create a Twitter app and obtain the API Key, API Secret, Access
Token, and Access Token Secret for the app. This can be done by
following the instructions at:
http://www.instructables.com/id/Raspberry-Pi-Twitterbot/?ALLSTEPS.

2. Override the corresponding strings in the file '.auth' with
appropriate Twitter app API access token strings obtained in the last
step.

3. Run 'python today_in_history_bot.py' to tweet.

4. (Optional) Create a cron job to invoke the bot once a day.
 
