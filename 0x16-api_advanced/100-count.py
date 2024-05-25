#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""

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

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not word_list or word_list == [] or not subreddit:
        return

    client_id = 'pX3xF8H_c5UVzcQ8xSrr7Q'
    secret = 'kfJcvQDuMcaOFN1y2bbLE82HPDi5Dg'
    token = get_token(client_id, secret)
    if not token:
        print("Error: Unable to get token")
        return

    url = "https://oauth.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/codeghinux)"
    }

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("Error occurred while fetching data. Response code:", response.status_code)
        print("Response content:", response.text)
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
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
        return "OK"

# Example usage:
if __name__ == "__main__":
    subreddit = "unpopular"
    word_list = ['down', 'vote', 'downvote', 'you', 'her', 'unpopular', 'politics']
    result = count_words(subreddit, word_list)
    print(result)
