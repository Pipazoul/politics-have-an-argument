# Attempt to request older tweets from username

import twitter
from gtts import gTTS
from playsound import playsound
import os
import re
from datetime import datetime
import shutil
import json 

# Getting configuration params
with open('config.json') as json_data_file:
    conf = json.load(json_data_file)

consumer_key = conf["consumer_key"]
consumer_secret = conf["consumer_secret"]
access_token_key = conf["access_token_key"]
access_token_secret = conf["access_token_secret"]


api = twitter.Api(consumer_key= consumer_key,
                  consumer_secret= consumer_secret,
                  access_token_key= access_token_key,
                  access_token_secret= access_token_secret)

def getPoliticTweet(account, language) :
    results = api.GetUserTimeline("",account, "", "", count, False, False, True)
    
    print(r"Getting tweet from :" + account)
    i = 1
    for result in results :
        if i <= tweetPerPolitic :
            # Make a function of all of this
            tweetDate = datetime.strptime(result.created_at, "%a %b %d %H:%M:%S +0000 %Y")
            if searchByMonth == True :
                if tweetDate.month == monthDate :
                    if querySearch == True :
                        if result.text.find(query) != -1 :
                            print(result.created_at)
                            result.text = re.sub(r'http\S+', '', result.text)
                            print(result.text)
                            genTTS(i, result, account,language)
                            i = i+1
                    else : 
                        print(result.created_at)
                        result.text = re.sub(r'http\S+', '', result.text)
                        print(result.text)
                        genTTS(i, result, account,language)
                        i = i+1
            else :
                if querySearch == True :
                    if result.text.find(query) != -1 :
                        print(result.created_at)
                        result.text = re.sub(r'http\S+', '', result.text)
                        print(result.text)
                        genTTS(i, result, account,language)
                        i = i+1
                else : 
                    print(result.created_at)
                    result.text = re.sub(r'http\S+', '', result.text)
                    print(result.text)
                    genTTS(i, result, account,language)
                    i = i+1
    print("################################")

def genTTS(i, result, account, language) :
    print("TTS Generation")
    if generateAudio == True :
            tts = gTTS(result.text, lang=language)
            
            if createSubFolders == True :
                try :
                    os.mkdir('output/'+account)
                except OSError :
                    print("The folders already exist")

                tts.save('output/'+account+'/audio'+ str(i) +'.mp3')
            else :
                tts.save('output/'+account+'_audio'+ str(i) +'.mp3')
            print(account)



generateAudio = True
createSubFolders = True

searchByMonth = False
querySearch =  True

count = 1000
tweetPerPolitic = 10
monthDate = 12
query = ""

if generateAudio == True :
    shutil.rmtree('output')
    os.mkdir('output')

#International politics
getPoliticTweet("realDonaldTrump", "en")
getPoliticTweet("borisjohnson", "en")
getPoliticTweet("barackobama", "en")
getPoliticTweet("AOC", "en")
getPoliticTweet("berniesanders", "en")
