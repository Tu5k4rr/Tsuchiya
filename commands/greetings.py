from discord.ext import commands
import discord, requests, json, random, os

#Setting up API key paths and files for gif services.
home = os.path.expanduser("~")
#Read in Giphy Key.
with open(f'{home}/Tsuchiya/keys/gifkey.txt', 'r') as gkey:
        gtoken = gkey.read()
#Read in Tenor Key.
with open(f'{home}/Tsuchiya/keys/tenor.txt', 'r') as tg:
        tkey = tg.read()


#Good morning gif.
def goodmorningcmd():
    gmturl = 'https://api.tenor.com/v1/random?q=goodmorning&key='
    gmtreq = requests.get(f'{gmturl}{tkey}')
    gmtjson = json.loads(gmtreq.content)
    gmtfinal = (gmtjson['results'][0]['url'])
    gmgurl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=goodmorning')
    reqgmif = requests.get(gmgurl)
    gmjson = json.loads(reqgmif.content)
    gffb = (gmjson['data']['embed_url'])
    gmrr = random.choice([gffb, gmtfinal])
    return gmrr

#Good afternoon gif.
def goodafternooncmd():
    gaturl = 'https://api.tenor.com/v1/random?q=goodafternoon&key='
    gatreq = requests.get(f'{gaturl}{tkey}')
    gatjson = json.loads(gatreq.content)
    gatfinal = (gatjson['results'][0]['url'])
    gagurl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=goodafternoon')
    gareqgmif = requests.get(gagurl)
    gajson = json.loads(gareqgmif.content)
    gaffb = (gajson['data']['embed_url'])
    garr = random.choice([gaffb, gatfinal])
    return garr

#Good evening gif.
def goodeveningcmd():
    gvturl = 'https://api.tenor.com/v1/random?q=goodafternight&key='
    gvtreq = requests.get(f'{gvturl}{tkey}')
    gvtjson = json.loads(gvtreq.content)
    gvtfinal = (gvtjson['results'][0]['url'])
    gvgurl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=goodnight')
    gvreqgmif = requests.get(gvgurl)
    gvjson = json.loads(gvreqgmif.content)
    gvffb = (gvjson['data']['embed_url'])
    gvrr = random.choice([gvffb, gvtfinal])
    return gvrr

#Good night gif.
def goodnightcmd():
    gnturl = 'https://api.tenor.com/v1/random?q=goodafternight&key='
    gntreq = requests.get(f'{gnturl}{tkey}')
    gntjson = json.loads(gntreq.content)
    gntfinal = (gntjson['results'][0]['url'])
    gngurl = (f'https://api.giphy.com/v1/gifs/random?api_key={gtoken}&tag=goodnight')
    gnreqgmif = requests.get(gngurl)
    gnjson = json.loads(gnreqgmif.content)
    gnffb = (gnjson['data']['embed_url'])
    gnrr = random.choice([gnffb, gntfinal])
    return gnrr
