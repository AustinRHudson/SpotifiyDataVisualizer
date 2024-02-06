# Python program to read
# spotify json file and visualize data

import json
import os
import tkinter as tk

directory = os.fsencode("Data")

songCount = {}

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename = "data/" + filename

    # Opening JSON file
    fileData = open(filename, errors="ignore")

    # returns JSON object as
    # a dictionary
    spotifyData = json.load(fileData)

    # Iterating through the json
    # list
    for i in spotifyData:
        if(i['master_metadata_track_name'] in songCount):
            songCount[i['master_metadata_track_name']] = songCount[i['master_metadata_track_name']] + 1
        else:
            songCount[i['master_metadata_track_name']] = 1
        #print(i["ts"])
        #print(i['master_metadata_track_name'])
    # Closing file
    fileData.close()

#Makes a list of the songs sorted from lowest amout of listens to highest.
songList = sorted(songCount, key=songCount.get, reverse=True)

#This will iterate through the dictionary and print them by the date they were added.
for key, value in songCount.items():
    print(key, value)

#This will iterate through the dictionary and print them by the frequency they appear.
for i in range(songCount.__len__()):
    print(songList[i])
    print(songCount[songList[i]])

window = tk.Tk()
window.geometry("1024x720")

songLabelList = []

for i in range(60):
    songLabelList.append(tk.Label(window, text = (songList[i], songCount[songList[i]], "times.")))
    songLabelList[i].config(font=("Times New Roman", 5))
    songLabelList[i].place(relx=1,rely=0 ,anchor='nw')
    songLabelList[i].pack()


window.mainloop()