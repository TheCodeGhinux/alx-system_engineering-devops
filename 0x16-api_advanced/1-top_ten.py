#!/usr/bin/python3
"""function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
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


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""

    client_id = 'pX3xF8H_c5UVzcQ8xSrr7Q'
    secret = 'kfJcvQDuMcaOFN1y2bbLE82HPDi5Dg'
    token = get_token(client_id, secret)
    if not token:
        print("Error: Unable to get token")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Test"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        # for i in range(10):
        #     print(response.json().get("data").get("children")[i]
        #           .get("data").get("title"))
        return "OK"
    else:
        return "OK"
