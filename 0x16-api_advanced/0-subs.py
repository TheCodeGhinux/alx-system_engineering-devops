#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for
a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hdrs = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)"}

    response = requests.get(url, headers=hdrs,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
    
# Test the function with the subreddit "programming"
if __name__ == "__main__":
    subreddit = "programming"
    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")