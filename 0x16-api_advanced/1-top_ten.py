#!/usr/bin/python3
"""0x16 - 1"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for subreddit"""
    rsr = requests.get('https://api.reddit.com/r/{}/hot.json'
                       .format(subreddit), headers={'User-Agent': 'nibroc'},
                       allow_redirects=False).json()
    try:
        hots = rsr.get('data').get('children')
        i = 0
        while i < 10:
            print(hots[i].get('data').get('title'))
            i += 1
    except:
        print(None)
