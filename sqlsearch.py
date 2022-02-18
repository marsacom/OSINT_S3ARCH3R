#!/usr/bin/env python3

# This script allows for you to automatically search for .com sites given
# a google dork (or anything really) to perform SQL Injections, and have the results displayed!

# DISCLAIMER: This script is NOT to be used to perform malicous activity,
# you and ONLY you are responsible for your actions when using this script!


import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

try:
	from googlesearch import search
except ImportError:
	print(f'{Fore.RED}{Style.BRIGHT}"Google" was not found!')

print(f'{Fore.CYAN}{Style.BRIGHT}Be sure to use quatation marks around your search for an exact result!')

print('-----------------------------------------------------------------------')


# Takes search term input from user
searchterm = input(f'{Fore.GREEN}Input your desired search term...{Fore.WHITE}')

# Takes number of searches desired input from user
searchnumber = input(f'{Fore.GREEN}Input your desired amount of search results...{Fore.WHITE}')

# Turns number input into an integter
searchnumber = int(searchnumber)

# Searches google with your desired parameters 
for i in search(searchterm, tld="com", num=searchnumber, stop=searchnumber, pause=2):
	print(Fore.WHITE + i)