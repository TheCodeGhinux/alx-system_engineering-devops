#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for
a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "YourAppName/1.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            subreddit_info = response.json()
            return subreddit_info["data"]["subscribers"]
        elif response.status_code == 404:
            return 0
        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Exception: {e}")
        return 0
