import requests
import json

username = 'bit-web24'
token    = ''
url      = "https://api.github.com/users/{}".format(username)

userdata = requests.get(url).json()
DATA = {
    "username"  : userdata['login'],
    "email"     : userdata['email'],
    "followers" : str(userdata['followers']),
    "following" : str(userdata['following']),
    "joined_at" : userdata['created_at'],
    "location"  : userdata['location'],
    "repos"     : []
}

userdata   = requests.get(url+ '/repos').json()
repo_count = len(userdata)

for n in range(0, repo_count):
    license = "NULL"
    keys = ['name', 'created_at', 'language', 'visibility', 'default_branch', 'forks']
    repo_data = {}

    try:
        license = userdata[n]["license"]["name"]
    except:
        pass

    for s in keys:
        repo_data[s] = userdata[n][s]

    repo_data['license'] = license
    DATA['repos'].append(repo_data)

with open('github.json', 'w') as json_file:
    json.dump(DATA, json_file, indent = 4)
