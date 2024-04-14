#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        allow_redirects=False  # Prevent following redirects
    )

    if req.status_code == 200:
        data = req.json().get("data", {})
        if "subscribers" in data:
            return data["subscribers"]
        else:
            return 0
    else:
        return 0
