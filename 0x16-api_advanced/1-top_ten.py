#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for invalid response status

        data = response.json().get("data")
        if not data:
            print("None")
            return

        children = data.get("children")
        if not children:
            print("None")
            return

        for i, child in enumerate(children[:10]):
            title = child.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print("[No title]")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        print("None")
