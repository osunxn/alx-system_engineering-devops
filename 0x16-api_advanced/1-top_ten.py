#!/usr/bin/python3
"""
1-top_ten
"""
import requests
import json


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data[:10]:
                print(post.get('data').get('title'))
        else:
            print(None)
    except json.JSONDecodeError:
        print(None)
