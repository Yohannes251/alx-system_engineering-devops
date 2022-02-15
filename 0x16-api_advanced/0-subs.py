#!/usr/bin/python3
"""
    This script defines a function that queries the Reddit api
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""

    headers = {'User-Agent': 'test_api/0.0.1'}
    url = 'https://www.reddit.com/r/{:s}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    return (response.json().get("data").get("subscribers"))
