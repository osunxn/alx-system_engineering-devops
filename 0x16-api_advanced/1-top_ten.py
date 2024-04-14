#!/usr/bin/python3
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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        data = req.json().get("data", {}).get("children", [])
        for post in data:
            title = post.get("data", {}).get("title")
            print(title)
    elif req.status_code == 404:
        print("None")
    else:
        print(None)
