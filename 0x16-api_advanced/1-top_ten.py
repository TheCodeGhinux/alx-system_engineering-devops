#!/usr/bin/python3
"""function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "YourAppName/1.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            posts_data = response.json()["data"]["children"]
            for post in posts_data[:10]:
                print(post["data"]["title"])
        elif response.status_code == 404:
            print(None)
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
