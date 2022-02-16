#!/usr/bin/python3
"""
    This script defines a function that queries the Reddit api
"""

import requests


def count_words(subreddit, word_list, count=0, after=''):
    """Returns titles of all hot posts of a subreddit"""

    headers = {'User-Agent': 'test_api/0.0.1'}
    params = {
            "count": count,
            "after": after
            }
    url = 'https://www.reddit.com/r/{:s}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=headers,
                            allow_redirects=False,
                            params=params)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
