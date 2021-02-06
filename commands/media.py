from discord.ext import commands
import discord, requests, json, random, os

#Setting up path for resources
home = os.path.expanduser("~")
#Read in Giphy Key.
with open(f'{home}/Tsuchiya/resources/eurobeat.json', 'r') as jeuro:
        eudata = json.load(jeuro)
    
#Picking Random EuroBeat Song.
def eurobeatcmd ():
    gasgasgas = random.choice(eudata)
    return gasgasgas
