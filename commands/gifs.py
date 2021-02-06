from discord.ext import commands
import discord, requests, json, random, os


#Setting up API key paths and files for gif services.
home = os.path.expanduser("~")
#Read in Giphy Key.
with open(f'{home}/Tsuchiya/gifkey.txt', 'r') as gkey:
        gtoken = gkey.read()
#Read in Tenor Key.
with open(f'{home}/Tsuchiya/keys/tenor.txt', 'r') as tg:
        tkey = tg.read()

#Happy Birthday
def happycmd():
    happyurl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=happybirthday')
    reqhappy = requests.get(happyurl)
    jsonhappy = json.loads(reqhappy.content)
    reshappy = (jsonhappy['data']['embed_url'])
    return reshappy

#Random Gif from Tenor or Giphy
def rgifcmd():
    turl = 'https://api.tenor.com/v1/random?q=%s&key='
    treq = requests.get(f'{turl}{tkey}')
    tjson = json.loads(treq.content)
    tfinal = (tjson['results'][0]['url'])
    gurl = 'https://api.giphy.com/v1/gifs/random?api_key='
    bgurl = (f'{gurl}{gtoken}')
    reqbgif = requests.get(bgurl)
    bgjson = json.loads(reqbgif.content)
    ffb = (bgjson['data']['embed_url'])
    rr = random.choice([ffb, tfinal])
    return rr

# Weeb Command for gifs matching "Weeb" - Request by Sanderpy.
def weebcmd():
    weeburl = 'https://api.tenor.com/v1/random?q=weeb&key='
    weebreq = requests.get(f'{weeburl}{tkey}')
    weebjson = json.loads(weebreq.content)
    weebfinal = (weebjson['results'][0]['url'])
    gweeburl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=goodnight')
    weebgg = requests.get(gweeburl)
    gweebjson = json.loads(weebgg.content)
    gw = (gweebjson['data']['embed_url'])
    wrr = random.choice([gw, weebfinal])
    return wrr
