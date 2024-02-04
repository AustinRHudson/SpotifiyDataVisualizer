# Python program to read
# json file

import json
import os

# Opening JSON file



directory = os.fsencode("Data")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename = "data/" + filename
    fileData = open(filename, errors="ignore")
    spotifyData = json.load(fileData)
    for i in spotifyData:
        print(i["ts"])
        print(i['master_metadata_track_name'])
    fileData.close()

# returns JSON object as
# a dictionary


# Iterating through the json
# list



# Closing file
