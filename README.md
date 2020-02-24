# politics-have-an-argument
Art Installation 

## Requirements
twitter
gtts


> pip install -r requirements.txt

## How it works
20 speakers with raspberrypi ? :
- receiver.py (gets every audio file)
- player.py (plays audio files and changes motor rotation -> sends an osc message when file finished playing)
1 Main server :
- request.py Grabs tweets and generates audio
- sender.py Sends audio files to raspberry's
- When all rapsberry finished playing files -> Generates audio files again ?


# 5 minutes de tweet par package
# FR : Benoi amont - Laurent vauquiez - François Bayrou - Yannick Jadot - Nicolas Hulot - François Hollande - 
# ENG : Trump - Boris Jhonson - Bolsonarro - Obama - Alexandrie Ocasio cortes - Bernie Sanders - Mercel - Salvini - 
# Dicture mode : 

15 Politiques / 3 tweet (en moyenne) par politique / chacun parle à son tour  = 5min40 de conversation

32kbt/s max icecast


# TODO :
Envoier un flux sur le serveur icecast avec ffmpeg ou ezcquelquechose
url : localhost:8000/stream
login : source
psswd : l'habituel

Tester des chemins twitter differents
Faciliter le lancement des (fichier de configs)
Maybe :

## Wording
Totem = Speaker
