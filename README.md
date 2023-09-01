# dirENUM
A python script that utilizes requests and a wordlist to discover directories/pages.

*Intended for Unix-like systems utilizing ANSI escape codes for colored text, output will look off on Windows but should maintain functionality.*

Libraries:

- Requests (2.31.0)
- Sys
- OS



## Prerequisites

- Python (3.7 or newer)
- Pip


## Installation

- Download and unzip this repo
- Run this command from within the repo folder

   `pip install -r requirements.txt`
   
- Run the dirENUM.py file with the URL and wordlist as arguments

   `python3 dirENUM.py http://10.0.0.1 wordlist.txt`
