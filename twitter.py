from __future__ import unicode_literals
import os
print(os.environ)
from flask import Flask, render_template, request, redirect
from requests_oauthlib import OAuth1Session


import dotenv
dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_key = consumer_key.encode('utf-8')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
consumer_secret = consumer_secret.encode('utf-8')

access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token = access_token.encode('utf-8')

access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
access_token_secret = access_token_secret.encode('utf-8')



session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

# The contents of status (i.e. tweet text)
status = 'If you are reading this on Twitter, the API request worked!'

# Send a POST request to the url with a 'status' parameter
resp = session.post(url, { 'status': status })

# Show the text from the response
print(resp.text)

def tweet(status):
    resp = session.post(url, { 'status': status })
    return resp.text
