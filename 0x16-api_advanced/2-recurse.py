#!/usr/bin/python3
"""function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit
"""

import requests


def get_token(client_id, secret):
    auth = requests.auth.HTTPBasicAuth(client_id, secret)
    data = {
        'grant_type': 'client_credentials'
    }
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)'
    }
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json().get('access_token')
    return token


def recurse(subreddit, hot_list=None, after=None):

    client_id = 'pX3xF8H_c5UVzcQ8xSrr7Q'
    secret = 'kfJcvQDuMcaOFN1y2bbLE82HPDi5Dg'
    token = get_token(client_id, secret)
    if not token:
        print("Error: Unable to get token")
        return

    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)"
    }
    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                                params=params)
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception as e:
        print(f"Exception: {e}")
        return None
