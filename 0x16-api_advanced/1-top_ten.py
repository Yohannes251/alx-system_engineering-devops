#!/usr/bin/python3
"""
    This script defines a function that queries the Reddit api
"""

import requests


def top_ten(subreddit):
    """Returns titles of the first ten hot posts of a subreddit"""

    headers = {'User-Agent': 'test_api/0.0.1'}
    url = 'https://www.reddit.com/r/{:s}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params={"limit": 10})

    if response.status_code == 404:
        print(None)
        return

    data = response.json().get("data")
    for child in data.get("children"):
        print(child.get("data").get("title"))
