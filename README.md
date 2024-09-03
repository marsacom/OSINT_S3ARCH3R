# OSINT_S3ARCH3R

![logo](https://github.com/marsacom/OSINT_S3ARCH3R/blob/main/img/image.png)

This is a script to run automatic searches through google to find URLs, given a search term/google-dork, for use in OSINT & Google Dorking!

## Installation
Step 1. ``git clone https://github.com/marsacom/OSINT_S3ARCH3R.git``

Step 2. ``pip3 install -r requirements.txt``

## Usage
``python3 osearcher.py -t YOUR-SEARCH -n NUM-OF-SEARCHES (-p PAUSE-INTERVAL) (-o OUTPUT-FILE)``

## Example Usage
#### OSINT
``python3 osearcher.py -t "John Doe" -n 20 -p 4 -o johndoe.txt``
#### Google Dorks
``python3 osearcher.py -t inurl:"store/products.php?productid=" -n 25 -p 5 -o productsphp.txt`` 

## Arguements
> ``-t``/``--term`` : 
>
> #### **The term/google-dork to search for...**
>
> - ***ex. -t "YOUR TARGETS NAME" or -t inurl:"store/products.php?productid=" (Use "" for EXACT results)***
>
> ``-n``/``--number`` : 
>
> #### **The number of URLs to generate...** 
>
> - ***ex. -n 10***
>
> ``-p``/``--pause`` : 
>
> #### **OPTIONAL: The lapse to wait between HTTP requests, measured in ***seconds***. Default is 2...**
>
> - ***ex. -p 4 (too short may cause Google to BLOCK your IP)***
>
> ``-o``/``--output`` : 
>
> #### **OPTIONAL: The name of the file to output results too...**
>
> - ***ex. -o results.txt, -o output.txt***

# Future Updates & Features
* Search for ***multiple*** specific terms/dorks

    > Ability to search for multiple specific terms/dorks will allow for more refined search results

* Proxy support     

    > Proxy support will provide advanced measures for avoiding detection from Google while running the script

# DISCLAIMER
This script allows you to automatically search Google, given this, Google could block your IP from searching due to the automation of the script seen as a potential DDOS attack with all the HTTP requests. This is why the *pause* is automatically set to 2. If you want to change that to make the script run faster you can via ``-p``/``--pause``. Likewise if you would like to slow down the time between requests to be extra safe you can make this vaule higher.

This script is NOT to be used to perform malicous activity. Any and all such activities are highly discouraged. You and ONLY you are responsible for your actions when using this script!

Author : Brayden Kukla 2024
