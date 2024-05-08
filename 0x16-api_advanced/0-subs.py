#!/usr/bin/python3
"""function that returns the number of subscribers"""

import requests

def number_of_subscribers (subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data.get("data").get("subscribers")
    else:
        return 0
