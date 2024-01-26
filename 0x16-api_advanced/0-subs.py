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
    headers = {"User-Agent": "advanced.api/1.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses

        # Check if there is a redirect and follow it
        if response.is_redirect:
            redirected_url = response.headers['Location']
            response = requests.get(redirected_url, headers=headers)
            response.raise_for_status()

        results = response.json().get("data")
        return results.get("subscribers")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return 0
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Exception: {e}")
        return 0
