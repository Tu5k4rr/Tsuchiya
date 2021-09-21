#Importing scripts and functions along with required libraries.
from commands import fun, gifs, media, webstuff, subred
from discord.ext import commands
import discord
import os

#Setup loading vars and data
#cwd
cwd = os.getcwd()

#Reading in Discord API Key
with open(f'{cwd}/keys/token.txt', 'r') as botkey:
   token = botkey.read()

#Reading in Data
#Decalring discord bot varibles.
client = discord.Client()
client = commands.Bot(command_prefix = '!', case_insensitive=True)

#Decalring functions
#Fun functions
@client.command()
async def coin (ctx):
    await ctx.send(fun.coin())

@client.command()
async def red (ctx):
    await ctx.send(subred.reddit())

@client.command()
async def roll (ctx):
    await ctx.send(fun.rollcmd())

@client.command()
async def ball (ctx):
    await ctx.send(fun.ballcmd())

@client.command()
async def rate (ctx):
    await ctx.send(fun.ratecmd())

@client.command()
async def ud (ctx):
    await ctx.send(embed=fun.udcmd())


@client.command()
async def twitch (ctx):
    await ctx.send(subred.twit())



#gif functions
@client.command()
async def rgif (ctx):
    await ctx.send(gifs.r_choice())

@client.command()
async def eurobeat (ctx):
    await ctx.send(media.eurobeatcmd())


#web functions
@client.command()
async def rwiki (ctx):
    await ctx.send(webstuff.rwikicmd())

@client.command()
async def wikitoday (ctx):
    await ctx.send(webstuff.wikitodaycmd())

#start bot
client.run(token)
