# dirENUM
import os
import sys
import requests

directoryExists = []  # List for directories that come back with a 200
input_error = 'False'

GREEN = '\033[92m'  # Green text color
RED = '\033[91m'  # Red text color
BLUE = '\033[94m'  # Blue text color
RESET = '\033[0m'  # Default text color


def directory_enumerate(provided_url, provided_wordlist, show_requests):
    try:
        wordlist_location = os.path.join(os.getcwd(), provided_wordlist)
        with open(provided_wordlist, 'r') as f:
            wordlist = f.read().splitlines()
            line_total = len(wordlist)

        print("\n==================================")
        print(BLUE + "./#dirENUM#\.")
        print(RED + "URL: " + provided_url)
        print("Wordlist: " + wordlist_location)
        print("Total paths to test: ")
        print(line_total)
        print(RESET + "==================================\n")

        for item in wordlist:
            url = provided_url + '/' + item
            response = requests.get(url)
            if show_requests == 'False':
                if response.status_code == 200:
                    directoryExists.append(url)  # If the directory exists, add it to directoryExists
                    print("Request for", url, "- Status code:", response.status_code)
            elif show_requests == 'True':
                print("Request for", url, "- Status code:", response.status_code)
                if response.status_code == 200:
                    directoryExists.append(url)  # If the directory exists, add it to directoryExists

        print(GREEN + "\nDirectories found:")  # Lists all the paths that brought back a 200 in the request
        for directory in directoryExists:
            print(directory)
        print(RESET)

    except FileNotFoundError:
        print("The wordlist file was not provided/found!")
        print("Example: python3 direnum.py http://URL C:/wordlist.txt")
        sys.exit(1)


if len(sys.argv) != 3:
    print(GREEN + "Usage: python3 direnum.py http://URL wordlist.txt" + RESET)

try:
    provided_url = sys.argv[1]
except IndexError:
    print(RED + "Please provide the proper URL argument!" + RESET)
    sys.exit(1)

try:
    provided_wordlist = sys.argv[2]
except IndexError:
    print(RED + "Please provide the proper wordlist!" + RESET)
    sys.exit(1)

if len(sys.argv) == 3:
    user_response = input("Show requests being sent out?(Yes/No)")
    user_response = user_response.lower()

    if user_response == "yes":
        show_requests = 'True'
    elif user_response == "no":
        show_requests = 'False'
    else:
        print(RED + "Invalid input." + RESET)
        input_error = 'True'

    if input_error != 'True':
        directory_enumerate(provided_url, provided_wordlist, show_requests)
