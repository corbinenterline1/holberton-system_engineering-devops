#!/usr/bin/python3
"""0x16 - 0"""
import requests


def number_of_subscribers(subreddit):
    """Requests sub count from given subreddit, 0 if invalid"""
    rsr = requests.get('https://api.reddit.com/r/{}/about.json'
                       .format(subreddit), headers={'User-Agent': 'nibroc'},
                       allow_redirects=False).json()
    try:
        return rsr.get('data').get('subscribers')
    except:
        return(0)
