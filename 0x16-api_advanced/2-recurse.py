#!/usr/bin/python3
"""function that eturns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all hot articles"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'reconnect/1.0 (by nawal_khaled)'}
    params = {"after": after}
    res = requests.get(url, headers=headers, params=params)

    if res.status_code == 200:
        income = res.json().get('data').get('children')
        for i in income:
            data = i.get('data')
            title = data.get('title')
            hot_list.append('title')
        after = res.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
