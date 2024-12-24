#!/usr/bin/python3

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

# DISCLAIMER: This script is NOT to be used to perform malicous activity,
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
	sys.exit()

# Using CLI arguements now rather than the previous input() from user
parser = argparse.ArgumentParser(description='Generate a list of URLs from Google given a search term, built for faster OSINT & Google Dorking...')
parser.add_argument('-t', '--term', type=str, help='The term/google-dork to search for, ex. -t "YOUR TARGETS NAME" or -t "inurl:products.php?id=" (Use "" for EXACT results)', required=True)
parser.add_argument('-n', '--number', type=int, help='The number of URLs to generate, ex. -n 10', required=True)

# Optional args
parser.add_argument('-p', '--pause', type=int, help='OPTIONAL: The lapse to wait between HTTP requests, measured in seconds. Default is 2, (too short may cause Google to block your IP), ex. -p 2, -d 5', required=False)
parser.add_argument('-o', '--output', type=str, help='OPTIONAL: The name of the file to output results too, ex. -o results.txt, -o output.txt', required=False)

if len(sys.argv) < 5: 
	parser.print_help(sys.stderr)
	sys.exit(1)
 
args = parser.parse_args()

if args.pause != None:
	pause = args.pause
else:
	pause = 2

if args.output != None:
	f=open(args.output, 'w')
else:
	raise FileNotFoundError

print(f'{Fore.CYAN}{Style.BRIGHT}\nGenerating ' + str(args.number) + ' link(s) maching the term: ' + args.term + ' ... ')
print('-----------------------------------------------------------------------')

start = datetime.datetime.now()	# Get start time of search 
c = 0

# Searches google with the provided parameters 
for i in search(args.term, tld='com', num=args.number, stop=args.number, pause=pause):
	c = c + 1
	if args.term == '':
		print('UNKNOWN LINK')
	else:
		print(Fore.WHITE + i)
		if not FileNotFoundError:
			f.write(i + '\n')
			if c == args.number:
				stop = datetime.datetime.now()
				elaptime = (stop - start).total_seconds() * 1000
				print('\nResults saved to: ' + str(args.output) + '... ')
				f.write('\n' + str(args.number) + ' results matching term: ' + args.term + ' gathered in ' + str(elaptime) + ' milliseconds...')
				f.close