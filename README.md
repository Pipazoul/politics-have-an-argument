# politics-have-an-argument
Art Installation 

## Requirements
twitter
gtts

ezstream 
icecast server


> pip install -r requirements.txt

## How it works

![alt text](medias/architecture.jpg)

## Docker setup
Clone this repo
> git clone

cd politics-have-an-argument


Create a network so both containers can connect on the same subnet
>docker network create politics

Launch the icecast server with your own passwords
>docker run -p 8050:8000 -ti  --network=politics -e ICECAST_SOURCE_PASSWORD=mypassword -e ICECAST_ADMIN_PASSWORD=mypassword -e ICECAST_PASSWORD=mypassword -e ICECAST_RELAY_PASSWORD=mypassword moul/icecast 



**In another terminal**

>docker build -t politics .

>sudo docker run -ti --network=politics politics:latest 

In container :

> cp example.config.json config.json
> nano config.json

Replace the twitter api creditential by your own
https://dev.twitter.com/apps/new
```json
    "consumer_key":"consumer_key",
    "consumer_secret" :"consumer_secret",
    "access_token_key": "access_token_key",
    "access_token_secret" : "access_token_secret",

```
Then launch the start.sh file
> sh start.sh

**This will :**
- get the tweets 
- transcribe them to audio trough GTTS or Espeak
- Generate m3u playlists by politic
- Stream the audio trough /speaker1 /speaker2 /speaker3

**This process can take up to 1 minute**

## Audio Stream Specs
The shields used are :
- mp3Shield

A 32kbit/s second audiostream in mono




# 5 minutes de tweet par package
# FR : Benoi amont - Laurent vauquiez - François Bayrou - Yannick Jadot - Nicolas Hulot - François Hollande - 
# ENG : Trump - Boris Jhonson - Bolsonarro - Obama - Alexandrie Ocasio cortes - Bernie Sanders - Mercel - Salvini - 
# Dicture mode : 

15 Politiques / 3 tweet (en moyenne) par politique / chacun parle à son tour  = 5min40 de conversation

32kbt/s max icecast


# TODO :
- [ ] Pip requirement text file
- [ ] Choose between GTTS or Espeak
- [ ] Invastigate into WaweGan Tacotron models (ref CorentinJ)
- [ ] Web interface ?
- [ ] If no tweet found dig more into past tweets
- [ ] Create a priority system with speakers