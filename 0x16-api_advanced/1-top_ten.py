#!/usr/bin/python3
"""function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "advanced.api/1.0", }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 404:
          print("None")
          return
        results = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    except Exception as e:
        print(f"Exception: {e}")
