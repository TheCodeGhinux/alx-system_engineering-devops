#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not word_list or word_list == [] or not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "mozilla/5.0:0x16.api.advanced:v1.0.0"
                             "(by /u/codeghinux)"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("Error occurred while fetching data.")
        return

    data = response.json()
    children = data.get("data", {}).get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data.get("data", {}).get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
