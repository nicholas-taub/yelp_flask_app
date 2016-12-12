from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from os import environ 

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_businesses(location, term):
	auth = Oauth1Authenticator(
    consumer_key=environ['CONSUMER_KEY'],
    consumer_secret=environ['CONSUMER_SECRET'],
    token=environ['TOKEN'],
    token_secret=environ['TOKEN_SECRET']
	)

	client = Client(auth)
	
	params = {
	'term': 'food',
	'lang': 'en',
	'limit': 3
	}
	
	# This indicates the response we should be getting from Yelp
	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name})

	return businesses