import os
import sys    
import subprocess
import shutil
import json
import threading

# Getting configuration params
with open('./config.json') as json_data_file:
    conf = json.load(json_data_file)

path = "./" + conf["outputPath"]

# Speakers identification
#speaker1 = "./output/borisjohnson"
speaker1 = path + "/" + conf["speaker1"][1]
speaker2 = path + "/" + conf["speaker2"][1]
speaker3 = path + "/" + conf["speaker3"][1]


print(speaker1)





def thread_function(speaker):
    os.system("ezstream -c " + speaker + "/ezstream.xml")


if __name__ == "__main__":

    totem1 = threading.Thread(target=thread_function, args=(speaker1,))
    totem1.start()
    totem2 = threading.Thread(target=thread_function, args=(speaker2,))
    totem2.start()
    #totem3 = threading.Thread(target=thread_function, args=(speaker3,))
    #totem3.start()