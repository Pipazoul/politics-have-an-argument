# Attempt to request older tweets from username

import twitter
from gtts import gTTS
import os
import re
from datetime import datetime
import shutil
import json 
import subprocess


# Getting configuration params
with open('./config.json') as json_data_file:
    conf = json.load(json_data_file)

# API Credentials
consumer_key = conf["consumer_key"]
consumer_secret = conf["consumer_secret"]
access_token_key = conf["access_token_key"]
access_token_secret = conf["access_token_secret"]

# Searching params
generateAudio = True
createSubFolders = True

searchByMonth = conf["searchByMonth"]
querySearch =  True

count = conf["tweet_count"]
tweetPerPolitic = conf["tweet_number"]
monthDate = conf["monthDate"]
query = conf["query"]
outputPath = "./" + conf["outputPath"]
# Speakers identification
speaker1 = conf["speaker1"]
speaker2 = conf["speaker2"]
speaker3 = conf["speaker3"]



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
                    os.mkdir(outputPath+'/'+account)
                except OSError :
                    print("The folders already exist")

                tts.save(outputPath+'/'+account+'/audio'+ str(i) +'.mp3')
            else :
                tts.save(outputPath+'/'+account+'_audio'+ str(i) +'.mp3')
            print(account)


if generateAudio == True :
    try :
        shutil.rmtree(outputPath)
    except OSError :
        print("The folders already exist")
        os.mkdir(outputPath)
    try :
        os.mkdir(outputPath)
    except OSError :
        print("The folders already exist")

print("******************TWITTER TO TTS********************")
print("Numbers of tweet to search : " + str(count))
print("Tweet nb by user :" + str(tweetPerPolitic))
print("Search by month :" + str(searchByMonth))
if searchByMonth == True :
    print("Month number : " + str(monthDate))
print("Query : " + query)
print("****************************************************")


getPoliticTweet(speaker1[1], speaker1[2])
getPoliticTweet(speaker2[1], speaker1[2])
getPoliticTweet(speaker3[1], speaker1[2])

# python request_by_user.py realDonaldTrump en
#International politics
#getPoliticTweet("realDonaldTrump", "en")
#getPoliticTweet("borisjohnson", "en")
#getPoliticTweet("barackobama", "en")
#getPoliticTweet("AOC", "en")
#getPoliticTweet("berniesanders", "en")
