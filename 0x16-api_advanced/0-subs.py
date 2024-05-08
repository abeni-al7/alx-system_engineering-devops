#!/usr/bin/python3
"""This script has a function that queries the Reddit API and returns the number of all subscribers
for a given subreddit"""


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
