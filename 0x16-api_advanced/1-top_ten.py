#!/usr/bin/python3
"""function that prints the titles of the first 10 hot posts listed"""

import requests


def top_ten(subreddit):
    """print top 10 titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'reconnect/1.0 (by nawal_khaled)'}

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        income = res.json().get('data').get('children')
        for i in range(10):
            print(income[i].get('data').get('title'))
    else:
        print('None')
