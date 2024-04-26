#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        data = response.json().get('data')
        if response.status_code == 200 and data:
            children = data.get('children')
            if children:
                for post in children[:10]:
                    print(post.get('data').get('title'))
                return
    except ValueError:  # JSONDecodeError in Python 3.5 and earlier
        pass  # Print None if there's an issue with JSON parsing
    print(None)
