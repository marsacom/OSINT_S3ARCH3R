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

print('Initializing OSINT_SEARCHER, please wait...')

import sys	
import colorama
import datetime
import argparse
import json
import random
import requests
from colorama import Fore, Style
from googlesearch import search
from textblob import TextBlob
from bs4 import BeautifulSoup

colorama.init(autoreset=True)

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	'Mozilla/5.0 (Linux; Android 8.1.0; TA-1032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
]

proxy_lists = [
	None,	
	# No proxies by default
	# Uncomment and add your proxies if needed
	# 'http://user:pass@proxyserver:port',
	# 'https://user:pass@proxyserver:port'
]

# Required args
# parser = argparse.ArgumentParser(description='Generate a list of URLs from Google given a search term, built for faster OSINT & Google Dorking...')
# parser.add_argument('-t', '--term', type=str, help='The term/google-dork to search for, ex. -t "YOUR TARGETS NAME" or -t inurl:"products.php?id=" (Use "" for EXACT results)', required=True)
# parser.add_argument('-n', '--number', type=int, help='The number of URLs to generate, ex. -n 10', required=True)

# # Optional args
# parser.add_argument('-p', '--pause', type=int, default=2, help='OPTIONAL: The lapse to wait between HTTP requests, measured in seconds, ex. -p 2, -d 5 (Default is 2, too short may cause Google to block your IP)', required=False)
# parser.add_argument('-o', '--output', type=str, help='OPTIONAL: The name of the file to output results too, ex. -o results.txt, -o output.txt', required=False)
# parser.add_argument('-l','--location', type=str, help='OPTIONAL: Filter results by location keyword, ex. --location "New York"', required=False)

# args = parser.parse_args()

# term = args.term if args.term else ''
# number = args.number if args.number else 0
# pause = args.pause if args.pause else 2
# output = args.output if args.output else None
# location = args.location if args.location else None

# Formatting function for search terms
def in_quotes(value):
    if not (value.startswith('"') and value.endswith('"')) and not (value.startswith("'") and value.endswith("'")):
        return f'"{value}"'
    return value

# Fetch page title & analyze content 
def fetch_page_data(url):
	headers = {'User-Agent': random.choice(user_agents)}
	proxy = random.choice(proxy_lists) if proxy_lists else None
	proxies = {'http': proxy, 'https': proxy} if proxy else None

	try:
		resp = requests.get(url, headers=headers, proxies=proxies, timeout=5)
		soup = BeautifulSoup(resp.text, 'html.parser')
		title = soup.title.string if soup.title else 'No title'
		text = ' '.join([p.text for p in soup.find_all('p')])[:500]  # Extract snippet
		sentiment = TextBlob(text).sentiment.polarity
		mentions_crime = any(word in text.lower() for word in ['arrest', 'fraud', 'crime', 'lawsuit', 'charged', 'court'])
		return title, text[:200], sentiment, mentions_crime
	except Exception:
		return 'N/A', '', 0, False

# Determine source type and classify it
def classify_source(url):
	sources = []
	if any(x in url for x in ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']): sources.append('social')
	if any(x in url for x in ['news', 'blog', 'press']): sources.append('news')
	if any(x in url for x in ['wikipedia.org', 'about', 'info', 'wiki']): sources.append('informational')
	if any(x in url for x in ['gov']): sources.append('government')
	if any(x in url for x in ['edu']): sources.append('education')
	if any(x in url for x in ['forum', 'discussion', 'community']): sources.append('forum')
	if not sources: sources.append('other')
	return ', '.join(sources)	

def osint_search(term, number, pause, location):
	global count
	global urls
	global results

	count = 0  # Initialize counter for number of results found
	urls = set()  # Initialize set to store unique URLs
	results = []  # Initialize list to store results

	term = f'intext:{term}'

	if location:
		term = term + ' AND ' + f'intext:{location}'  # Append location to search term if provided

	for url in search(term, num=number, stop=number, pause=pause):
		title, snippet, sentiment, crime_flag = fetch_page_data(url)
		confidence = 0.7 if crime_flag else 0.5 + abs(sentiment)/2

		count += 1  # Increment counter for each URL found
			
		data = {
			'url': url,
			'title': title,
			'snippet': snippet,
			'source_type': classify_source(url),
			'mentions_crime': crime_flag,
			'sentiment': sentiment,
			'confidence': round(confidence, 2)
		}

		if url not in urls:  # Check for duplicates
			results.append(data)
			urls.add(url)

		print(f"{Fore.WHITE}{url} | {Fore.YELLOW}{data['source_type']} | {Fore.GREEN}Conf:{data['confidence']}")

try:
	print(f'{Fore.GREEN}{Style.BRIGHT}Script initilization successful!')
	term = in_quotes(input(f'{Fore.CYAN}{Style.BRIGHT}Enter search term (e.g., "John Doe"): ').strip())
	number = int(input(f'{Fore.CYAN}{Style.BRIGHT}Enter number of results to generate (e.g., 10): ').strip())
	location = in_quotes(input(f'{Fore.CYAN}{Style.BRIGHT}Enter location filter (optional, press Enter to skip): ').strip()) or None
	output = input(f'{Fore.CYAN}{Style.BRIGHT}Enter output file name (optional, press Enter to skip): ').strip() or None
	output = (output + '.json') if output and not output.endswith('.json') else output  # Ensure .json extension
	pause = int(input(f'{Fore.CYAN}{Style.BRIGHT}Enter pause between requests (in seconds, default 2): ').strip() or 2)

	if term != '' and number > 0 : # Only searching if they actually passed a term and/or number of results 
		print(f'{Fore.CYAN}{Style.BRIGHT}\nGenerating {number} link(s) maching the term: {term}' + (f' and location: {location}' if location is not None else ''))
		print('-----------------------------------------------------------------------')
		start = datetime.datetime.now()  # Get start time of search 

		osint_search(term, number, pause, location)

		stop = datetime.datetime.now()
		elaptime = (stop - start).total_seconds() 
		print(f'{Fore.GREEN}{Style.BRIGHT}\nSearch completed in {elaptime:.2f} seconds, found {count} results matching term: {term}' + (f' and location: {location}' if location is not None else ''))

		if output:
			with open(output, 'w') as f:
				json.dump(results, f, indent=4)

			print(f'{Fore.GREEN}Results saved to {output}')
			f.close()
	else:
		print(f'{Fore.RED}{Style.BRIGHT}No search term and/or number of results to generate specified, exiting script...')
		sys.exit(0)		

except KeyboardInterrupt:
	print(f'{Fore.RED}{Style.BRIGHT}\n\nInterrupted by user, exiting script...')
	sys.exit(0)