from playsound import playsound
import os
from threading import Thread # For multi Threading
import threading


def playPoliticTweet(account, language) :
#Gets every mp3 file in folder
    def mp3gen():
        for root, dirs, files in os.walk('output/'+account+'/'):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3":
                    yield os.path.join(root, filename)

    # Plays every mp3 file in folder
    for mp3file in sorted(mp3gen()):
        print mp3file
        playsound(mp3file)



# French politics
playPoliticTweet("benoithamon", "fr")
playPoliticTweet("laurentwauquiez", "fr")
playPoliticTweet("bayrou", "fr")
playPoliticTweet("yjadot", "fr")
playPoliticTweet("N_Hulot", "fr")
playPoliticTweet("fhollande", "fr")
playPoliticTweet("JLMelenchon", "fr")
playPoliticTweet("MLP_officiel", "fr")

#International politics
playPoliticTweet("realDonaldTrump", "en")
playPoliticTweet("borisjohnson", "en")
playPoliticTweet("barackobama", "en")
playPoliticTweet("AOC", "en")
playPoliticTweet("berniesanders", "en")
#playPoliticTweet("AngelaMerkeICDU", "de")
playPoliticTweet("matteosalvinimi", "it")
playPoliticTweet("jairbolsonaro", "es")
