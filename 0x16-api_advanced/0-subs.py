#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    try:
        req = requests.get(url, headers=headers)
        req.raise_for_status()  # Raise an exception for HTTP errors

        data = req.json().get("data")
        if data and "subscribers" in data:
            return data["subscribers"]
        else:
            return 0

    except requests.exceptions.RequestException as e:
        return 0
    except (KeyError, TypeError):
        # Handle exceptions for accessing nested keys or invalid JSON response
        return 0
