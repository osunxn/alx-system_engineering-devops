#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"after": after}

    try:
        req = requests.get(url, headers=headers, params=params)
        req.raise_for_status()  # Raise an error for invalid response status

        data = req.json().get("data")
        children = data.get("children")
        after = data.get("after")

        for child in children:
            hot_list.append(child.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        return None
