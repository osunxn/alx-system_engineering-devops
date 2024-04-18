#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    # Check if the response content is JSON
    try:
        data = response.json()
    except ValueError:  # If not JSON, print None
        print("None")
        return

    # Check if the subreddit exists
    if "error" in data:
        print("None")
        return

    # Extract and print titles of the posts
    for post in data.get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))
