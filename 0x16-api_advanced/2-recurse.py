#!/usr/bin/python3
"""function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "YourAppName/1.0"}
    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                                params=params)
        if response.status_code == 200:
            posts_data = response.json()["data"]["children"]
            titles = [post["data"]["title"]
                      for post in posts_data]
            hot_list.extend(titles)
            after = response.json()["data"].get("after")
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None
