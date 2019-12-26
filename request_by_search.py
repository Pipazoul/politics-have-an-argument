import twitter
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
from pydub import AudioSegment
import re
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
    # Twitter  Search Request
    results = api.GetSearch(
        raw_query="q="+query+"&from="+account+"&filter=links&since=2014-11-30&until=2015-11-30&count="+str(tweetNumber)+"")
        #raw_query="q="+query+"&from="+account+"&filter=links&result_type=recent&count="+str(tweetNumber)+"")

    shutil.rmtree('output')
    os.mkdir('output')
    # Generates GTTS audio for each tweet
    i = 0
    for result in results :
        result.text = re.sub(r'http\S+', '', result.text)
        print(result.text)
        if generateAudio == True :
            tts = gTTS(result.text, lang=language)
            
            if createSubFolders == True :
                try :
                    os.mkdir('output/'+account)
                except OSError :
                    print("The folders already exist")

                tts.save('output/'+account+'/audio'+ str(i) +'.mp3')
            else :
                #tts.save('output/audio'+ str(i) +'.mp3')
                tts.save('output/'+account+'_audio'+ str(i) +'.mp3')
            #sound = AudioSegment.from_mp3('audio'+ str(i) +'.mp3')
            #sound.export('audio'+ str(i) + '.wav', format="wav")
            print(account)
        i = i+1


    # Gets every mp3 file in folder
    def mp3gen():
        for root, dirs, files in os.walk('output'):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3":
                    yield os.path.join(root, filename)

    # Plays every mp3 file in folder
    for mp3file in sorted(mp3gen()):
        print (mp3file)
        if playAudio == True :
            playsound(mp3file)


generateAudio = False
createSubFolders = False
playAudio  = False
query = ""
date = "until=2018-11-30&since=2018-01-01"
tweetNumber = 3




# French politics
getPoliticTweet("benoithamon", "fr")
getPoliticTweet("laurentwauquiez", "fr")
getPoliticTweet("bayrou", "fr")
getPoliticTweet("yjadot", "fr")
getPoliticTweet("N_Hulot", "fr")
getPoliticTweet("fhollande", "fr")
getPoliticTweet("JLMelenchon", "fr")
getPoliticTweet("MLP_officiel", "fr")

#International politics
getPoliticTweet("realDonaldTrump", "en")
getPoliticTweet("borisjohnson", "en")
getPoliticTweet("barackobama", "en")
getPoliticTweet("AOC", "en")
getPoliticTweet("berniesanders", "en")
#getPoliticTweet("AngelaMerkeICDU", "de")
getPoliticTweet("matteosalvinimi", "it")
getPoliticTweet("jairbolsonaro", "es")
