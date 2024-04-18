#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests
import sys

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    # Check if subreddit exists
    exists = subreddit_exists(subreddit)
    if not exists:
        print(f"Subreddit '{subreddit}' does not exist.")
        return

    response = requests.get(url, headers=headers, params=params)

    # Check for HTTP errors
    if response.status_code != 200:
        print(f"Failed to retrieve data from Reddit: {response.status_code}")
        return

    data = response.json().get("data")
    if not data:
        print("No posts found.")
        return

    posts = data.get("children")
    for post in posts:
        print(post.get("data").get("title"))

def subreddit_exists(subreddit):
    """Check if a subreddit exists."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    return response.status_code == 200
