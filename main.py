#!/usr/bin/env python

# This program is mainly based on the book
# "Black Hat Python: Python Programming for Hackers
# and Pentesters" by Justin Seitz. This is just a 
# port to Python 3 with some minor tweaks.

import sys
import config, bruter, bruteparser
import urllib.request as urllib2


###################################################

def main():
	print("[+] Bootstrapping: ")

	if not bruteparser.bootstrap(config.target_url):
		print("[x] Bootstrapping error: No input-fields detected on target page.")
		print("[x] Exiting...")
		return
	

	words = config.build_wordlist(config.wordlist_file)

	try:
		html_page = urllib2.urlopen(config.target_url)
	except urllib.error.URLError:
		print("The site doesn't seem to be reachable: %s" % config.target_url)

	# Bootstrap the Bruter and look for hidden fields
	# that make the functionality of the page a bit
	# different.

	#brteparse = bruteparser.BruteParser()
	#brteparse.feed(str(html_page.read()))

	#brter = bruter.Bruter(config.username, words)
	#brter.run_bruteforce()

	#brteparse = bruteparser.BruteParser()
	#brteparse.feed(str(html_page.read()))
	#brteparse.return_pagetitle()

if __name__ == "__main__": main()