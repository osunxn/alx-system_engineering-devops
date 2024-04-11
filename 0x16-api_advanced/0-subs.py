#!/usr/bin/python3
'''
This module contains a function to retrieve the number of subscribers for a given subreddit.
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Returns the number of subscribers for a given subreddit.
    If the subreddit does not exist or an error occurs, returns 0.
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    # Retrieve the subreddit name from command-line arguments
    subreddit_name = argv[1]

    # Call the function and print the number of subscribers
    subscribers = number_of_subscribers(subreddit_name)
    if subscribers:
        print("Number of subscribers for r/{}: {}".format(subreddit_name, subscribers))
    else:
        print("Subreddit r/{} does not exist or an error occurred.".format(subreddit_name))
