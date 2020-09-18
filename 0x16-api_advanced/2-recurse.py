#!/usr/bin/python3
"""0x16 - 2"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles
    for a given subreddit, Rusing recursion"""
    if after is None:
        rsr = requests.get('https://api.reddit.com/r/{}/hot.json'
                           .format(subreddit),
                           headers={'User-Agent': 'nibroc'},
                           allow_redirects=False).json()
    else:
        rsr = requests.get('https://api.reddit.com/r/{}/hot.json?after={}'
                           .format(subreddit, after),
                           headers={'User-Agent': 'nibroc'},
                           allow_redirects=False).json()
    try:
        data = rsr.get('data')
        kidz = data.get('children')
    except:
        return(None)
    for kid in kidz:
        hot_list.append(kid.get('data').get('title'))
    after = data.get('after')
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
