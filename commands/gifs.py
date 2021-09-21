from discord.ext import commands
import discord, requests, json, random, os
#urls
#tenor
tenor = 'https://api.tenor.com'
#giphy
giphy = 'https://api.giphy.com'

#endpoint
tran = '/v1/random?q=%s&key='
gran = '/v1/gifs/random?api_key='

#Setting up API key paths and files for gif services.
cwd = os.getcwd()
#tenor key
with open(f'{cwd}/keys/tenor.txt', 'r') as tkey:
    ttoken = tkey.read()

#giphy key
with open(f'{cwd}/keys/giphy.txt', 'r') as gkey:
   gtoken = gkey.read()

def func_rtenor():
    tt =  f'{tenor}{tran}{ttoken}'
    t_req = requests.get(f'{tenor}{tran}{ttoken}')
    tjson = json.loads(t_req.content)
    tres = (tjson['results'][0]['url'])
    return tres

def func_rgiphy():
    g_req = requests.get(f'{giphy}{gran}{gtoken}&tag=&rating=r')
    gjson = json.loads(g_req.content)
    gres = (gjson['data']['embed_url'])
    return gres

def_choice = [func_rgiphy, func_rtenor]

def r_choice():
    ret = random.choice(def_choice)()
    return ret
