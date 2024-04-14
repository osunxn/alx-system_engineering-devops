u#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    try:
        req = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json",
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
        )
        req.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = req.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

