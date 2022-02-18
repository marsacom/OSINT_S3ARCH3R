# SQLSearch
This is a simple python script to run automatic searches through google to find sites, given a google dork, for SQL Injections!

# Installation
Step 1. ``git clone https://github.com/marsacom/SQLSearch.git``

Step 2. ``pip3 install -r requirements.txt``

And that's it!

# Usage
``python3 sqlsearch.py``


Upon using this command you will be prompted to first input your desired search term and then desired number of results you want displayed. For example...``"inurl:products.php?id=4"`` for the search term and, ``10`` for the number of results!

# DISCLAIMER
This script allows you to automatically search Google, given this, Google could block your IP from searching due to the automation of the script seen as a potential DDOS attack with all the HTTP requests. This is why the pause is automatically set to 2, making the chances of this practically zero. If you want to change that to make the script run faster you can, but this could cause the blocking. Likewise if you would like to slow down the time between requests to be extra safe you can make this vaule higher.

This script is NOT to be used to perform malicous activity. Any and all such activities are highly discouraged. You and ONLY you are responsible for your actions when using this script!
