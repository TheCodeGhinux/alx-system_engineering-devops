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
    headers = {"User-Agent": "advanced.api/1.0"}

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 404:
          return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception as e:
        print(f"Exception: {e}")
        return 0
