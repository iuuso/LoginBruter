#!/usr/bin/env python

#
# Here are the different variables and
# parameters needed to run the program.
# 


###################################################
# General settings

import queue

user_thread 		= 10
username			= "admin"
wordlist_file		= "wordlists/10k_most_common.txt"
resume				= None
first_run			= True

token_names			= ["user_token", "authenticity_token"]

###################################################
# Target specific settings

target_url			= "http://localhost/login.php"
target_post			= "http://localhost/login.php"

username_field		= "username"
password_field		= "passwd"

###################################################
# Helper Functions

def build_wordlist(wordlist_file):
	fd = open(wordlist_file, "rb")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False
	words = queue.Queue()

	for word in raw_words:
		word = word.rstrip()
		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print("Resuming wordlist from: %s " % resume)
		else:
			words.put(word)

	print(" | Finished setting up wordlist from: %s" % wordlist_file)
	return words