#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for
a given subreddit. If an invalid subreddit
is given, the function should return 0.
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


def number_of_subscribers(subreddit):

    client_id = 'pX3xF8H_c5UVzcQ8xSrr7Q'
    secret = 'kfJcvQDuMcaOFN1y2bbLE82HPDi5Dg'
    token = get_token(client_id, secret)
    if not token:
        print("Error: Unable to get token")
        return

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)"
    }

    response = requests.get(url, headers=headers,
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
    print("The subreddit has {} subscribers.".format(subscribers))