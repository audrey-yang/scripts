'''
Find users you are following that aren't following you back

Requirements: followers_1.json, following.json in the same directory
    (obtain from data download)
'''

import json

followers, following = set(), set()

with open ('followers_1.json') as followers_file, \
    open('following.json') as following_file:
    followers_list = json.loads(followers_file.read())
    followers = set(
        [user["string_list_data"][0]["value"] for user in followers_list]
    )

    following_json = json.loads(following_file.read())
    following_list = following_json["relationships_following"]
    following = set(
        [user["string_list_data"][0]["value"] for user in following_list]
    )
    
for user in following.difference(followers):
    print(user)