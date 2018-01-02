#!/usr/bin/env python

import requests

from bs4 import BeautifulSoup

import config

def bootstrap(url):
	if config.first_run:
		page = requests.get(config.target_url)
		print(" | Page %s loaded successfully" % config.target_url)
		soup = BeautifulSoup(page.text, 'html.parser')

		inputs = soup.find_all("input")
		if not inputs:
			return False

		hiddenFields = soup.find_all('input', {'name': [x for x in config.token_names]})
		
		if not hiddenFields:

			# If no hidden fields can be found, this most likely
			# points out to the fact that there are no nonces
			# or CSRF-tokens etc. used in the application.

			return True

		print(type(hiddenFields))

		
		return True
	
	else: 
		return True

#class BruteParser(BeautifulSoup):
# 	def __init__(self):
# 		HTMLParser.__init__(self)
# 		self.tag_results = {}

# 		lsStartTags = list()
# 		lsEndTags = list()
# 		lsStartEndTags = list()
# 		lsComments = list()


# 	def handle_starttag(self, tag, attrs):

# 		if config.first_run:
# 			bootstrap(self, tag, attrs)

# 		if tag != "input":
# 			return
# 		#if tag == "input":

# 		for name, value in attrs:
# 			if name == "type" and value == "hidden":
# 				handle_hidden_token(name, value)
			
# 			tag_name = None
# 			tag_value = None
# 			#print(tag)

# 			for name, value in attrs:
# 				if name == "name":
# 					tag_name = value

# 				if name == "value":
# 					tag_value = value

# 			if tag_name is not None:
# 				self.tag_results[tag_name] = value

# 	def handle_hidden_token(field_name, field_value):

# 		# If the login form contains a hidden field with 
# 		# a CSRF token or a user token, return the value
# 		# If not, return False for token not found.

# 		if field_value in config.token_names:
# 			print("Hidden token found, using it")

# 			# If a token is found, then the situation changes drastically
# 			# in the case of brute-forcing since the hidden token often changes
# 			# every time the page is loaded. Therefore running 10 threads toward
# 			# the target page is unnecessary. 

# 			config.user_thread = 1

# 			# Please note this when considering the lengthened runtime

# 			# TODO: If a hidden field is found the function of this application
# 			# could change to 10 thread
# 		else:
# 			print("No hidden field found.")
# 			return False


# 	def return_pagetitle(self, data):
# 		if self.lsStartTags == "title":
# 			return data


# 		