#!/usr/bin/python3
"""Function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests
import sys


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
    if res.status_code == 200:
        token = res.json().get('access_token')
        return token
    else:
        print(f"Error: Unable to get token, status code {res.status_code}")
        return None


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""

    client_id = 'pX3xF8H_c5UVzcQ8xSrr7Q'
    secret = 'kfJcvQDuMcaOFN1y2bbLE82HPDi5Dg'
    token = get_token(client_id, secret)
    if not token:
        print("Error: Unable to get token")
        return

    url = f"https://oauth.reddit.com/r/{subreddit}/hot"
    headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            posts = response.json().get("data").get("children")
            for i in range(10):
                print(posts[i].get("data").get("title"))
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
    else:
        print(f"Error: Status code {response.status_code}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
