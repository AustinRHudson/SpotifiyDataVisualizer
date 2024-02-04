# Python program to read
# json file

import json

# Opening JSON file
f = open('Spotify2023-2024.json', errors="ignore")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print(i["ts"])
    print(i['master_metadata_track_name'])


# Closing file
f.close()