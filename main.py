import requests

username = 'bit-web24'
token    = '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'
url      = "https://api.github.com/users/{}".format(username)

userdata = requests.get(url).json()

print('userdata:')
print(' Username: ' + userdata['login'])
print(' Email: ' + str(userdata['email']))
print(' Followers: ' + str(userdata['followers']))
print(' Following: ' + str(userdata['following']))
print(' Joined-on: ' + userdata['created_at'])
print(' Location: ' + str(userdata['location']))

userdata = requests.get(url+ '/repos').json()
repo_count = len(userdata)

print('Repositories: ')
for n in range(0, repo_count):
    license = "Not Found"
    try:
        license = userdata[n]["license"]["name"]
    except:
        pass

    repo_data = """
        {}: {}
            created_at: {}
            language  : {}
            Visibility: {}
            Licence   : {}
            Default-branch: {}
            Forks     : {}
    """.format(str(n+1),
     userdata[n]['name'],
     userdata[n]['created_at'],
     userdata[n]['language'],
     userdata[n]['visibility'],
     license,
     userdata[n]['default_branch'],
     userdata[n]['forks'])
    print(repo_data)
