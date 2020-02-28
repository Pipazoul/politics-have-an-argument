import os
import sys    
import subprocess
import shutil
import json
from pathlib import Path

# Getting configuration params
with open('./config.json') as json_data_file:
    conf = json.load(json_data_file)

path = "./" + conf["outputPath"]

# Speakers identification
#speaker1 = "./output/borisjohnson"
speaker1 = path + "/" + conf["speaker1"][1]
speaker2 = path + "/" + conf["speaker2"][1]
speaker3 = path + "/" + conf["speaker3"][1]

# Stream config 
icecastUrl = conf["icecastUrl"]
icecastPassword = conf["icecastPassword"]


def generateConfigFiles(speakerPath,speakerName, icecastUrl, icecastPassword) :
    
    audioFiles = []
    files = os.listdir(speakerPath)
    pathFolder = Path(speakerPath).absolute()
    print(pathFolder)
    for file in sorted(files) : 
        # Checks the post type
        # Image checking
        if file.lower().endswith(('.mp3'))  :
            print(file)
            audioFiles.append(file)
        

    # Write playlist file
    file = open(speakerPath + "/" + "playlist.m3u","w") 
    file.write("#EXTM3U \n") 
    for audio in audioFiles :
        file.write("#EXTINF,"+ audio + "\n") 
        file.write(str(pathFolder) + "/" + audio + "\n") 
        print(audio)

    print("Playlist file generated : " + str(pathFolder) + "/")
    file.close() 
    # Write ezstream config file 
    file = open(speakerPath + "/" + "ezstream.xml","w") 
    file.write("<ezstream> \n") 
    file.write("    <url>"+icecastUrl + speakerName +"</url> \n")
    file.write("    <sourcepassword>"+icecastPassword +"</sourcepassword> \n")
    file.write("    <format>MP3</format> \n")
    file.write("    <filename>"+str(pathFolder) + "/playlist.m3u</filename> \n")
    file.write("    <stream_once>0</stream_once> \n")
    file.write("    <svrinfoname>Twitter username</svrinfoname> \n")
    file.write("    <svrinfobitrate>32</svrinfobitrate> \n")
    file.write("    <svrinfochannels>1</svrinfochannels> \n")
    file.write("    <svrinfosamplerate>44100</svrinfosamplerate> \n")
    file.write("    <svrinfopublic>1</svrinfopublic> \n")
    file.write("</ezstream> \n")
    file.close() 


generateConfigFiles(speaker1,"speaker1", icecastUrl, icecastPassword)
generateConfigFiles(speaker2,"speaker2", icecastUrl, icecastPassword)
generateConfigFiles(speaker3,"speaker3", icecastUrl, icecastPassword)
