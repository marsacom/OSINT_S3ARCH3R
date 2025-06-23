# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ┏━━━┳━━━┳━━┳━┓╋┏┳━━━━┓┏━━━┳━━━┳━━━┳━━━┳━━━┳┓╋┏┳━━━┳━━━┳━━━┓ #
# ┃┏━┓┃┏━┓┣┫┣┫┃┗┓┃┃┏┓┏┓┃┃┏━┓┃┏━┓┃┏━┓┃┏━┓┃┏━┓┃┃╋┃┃┏━┓┃┏━━┫┏━┓┃ #
# ┃┃╋┃┃┗━━┓┃┃┃┏┓┗┛┣┛┃┃┗┛┃┗━━╋┛┏┛┃┃╋┃┃┗━┛┃┃╋┗┫┗━┛┣┛┏┛┃┗━━┫┗━┛┃ #
# ┃┃╋┃┣━━┓┃┃┃┃┃┗┓┃┃╋┃┃╋╋┗━━┓┣┓┗┓┃┗━┛┃┏┓┏┫┃╋┏┫┏━┓┣┓┗┓┃┏━━┫┏┓┏┛ #
# ┃┗━┛┃┗━┛┣┫┣┫┃╋┃┃┃╋┃┃╋╋┃┗━┛┃┗━┛┃┏━┓┃┃┃┗┫┗━┛┃┃╋┃┃┗━┛┃┗━━┫┃┃┗┓ #
# ┗━━━┻━━━┻━━┻┛╋┗━┛╋┗┛╋╋┗━━━┻━━━┻┛╋┗┻┛┗━┻━━━┻┛╋┗┻━━━┻━━━┻┛┗━┛ #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# This script allows for you to automatically search for .com sites given
# a search term. Specifically designed for use in OSINT and Google Dorking

# DISCLAIMER: This script is NOT to be used to perform malicious activity,
# you and ONLY you are responsible for your actions when using this script!

# EXAMPLE USAGE: python3 sqlsearch.py -t "John Doe" -n 10 -p 3 -o johndoe.txt

# Author: Brayden Kukla 2024 

import sys	
import colorama
import datetime
import argparse
from colorama import Fore, Style

colorama.init(autoreset=True)

try: # Notify user of missing dependency
	from googlesearch import search
except ImportError:
	print(f'{Fore.RED}{Style.BRIGHT}ERROR: Package "googlesearch" was not found, please verify requirements installation...')
	exit(1)

# Using CLI arguments now rather than the previous input() from user
parser = argparse.ArgumentParser(description='Generate a list of URLs from Google given a search term, built for faster OSINT & Google Dorking...')
parser.add_argument('-t', '--term', type=str, help='The term/google-dork to search for, ex. -t "YOUR TARGETS NAME" or -t inurl:"products.php?id=" (Use "" for EXACT results)', required=True)
parser.add_argument('-n', '--number', type=int, help='The number of URLs to generate, ex. -n 10', required=True)

# Optional args
parser.add_argument('-p', '--pause', type=int, default=2, help='OPTIONAL: The lapse to wait between HTTP requests, measured in seconds, ex. -p 2, -d 5 (Default is 2, too short may cause Google to block your IP)', required=False)
parser.add_argument('-o', '--output', type=str, help='OPTIONAL: The name of the file to output results too, ex. -o results.txt, -o output.txt', required=False)
parser.add_argument('-tld', '--topleveldomain', type=str, default='com', help='OPTIONAL: The top-level domain to search, ex. -tld com, -tld uk, -tld ca (Default is "com")', required=False)

args = parser.parse_args()

try:
	if args.term.strip() == '' or args.number <= 0 : # Only searching if they actually passed a term and/or number of results 
		print(f'{Fore.RED}{Style.BRIGHT}No search term and/or number of results to generate specified, exiting script...')
		exit(0)	

	print(f'{Fore.CYAN}{Style.BRIGHT}\nGenerating {args.number} link(s) maching the term: {args.term}... ')
	print('-----------------------------------------------------------------------')

	start = datetime.datetime.now()	# Get start time of search 
	c = 0	# Initialize counter for number of results found
	urls = set() # Initialize set to store unique URLs

	# Searches google with the provided parameters 
	for i in search(args.term, tld=args.topleveldomain, num=args.number, stop=args.number, pause=args.pause):
		c += 1

		print(Fore.WHITE + i)
	
		if i not in urls: # Check for duplicates
			urls.add(i)
			
	stop = datetime.datetime.now()
	elaptime = (stop - start).total_seconds() * 1000
	print(f'{Fore.GREEN}{Style.BRIGHT}\nSearch completed in {elaptime:.2f} milliseconds, found {c} results matching term: {args.term}... ')

	if args.output:
		f=open(args.output, 'w')

		for url in urls:
			f.write(url + '\n')

		f.write('\nSearch completed in ' + str(elaptime) + ' milliseconds, found ' + str(c) + ' results matching term: ' + str(args.term) + '\n')
		f.close()
		print(f'{Fore.GREEN}{Style.NORMAL}\nResults saved to: ' + str(args.output) + '... ')

except KeyboardInterrupt:
	print(f'{Fore.RED}{Style.BRIGHT}\n\nInterrupted by user, exiting script...')
	sys.exit()