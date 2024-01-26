#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles, and
prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "YourAppName/1.0"}
    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                                params=params)


        if response.status_code == 200:
            posts_data = response.json()["data"]["children"]
            for post in posts_data:
                title = post["data"]["title"].lower()
                for word in word_list:
                    word = word.lower()
                    if word in title:
                        counts[word] = counts.get(word,
                                                  0) + title.count(word)
            after = response.json()["data"].get("after")
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                print_results(counts)
        elif response.status_code == 404:
            pass
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

def print_results(counts):
    sorted_counts = sorted(counts.items(),
                           key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
