#Importing scripts and functions along with required libraries.
from commands import fun, gifs, greetings, media, utils, webstuff
from discord.ext import commands
import discord
import os

#test
script_dir = os.path.dirname(__file__)

#cwd
cwd = os.getcwd()

#Reading in apikey
with open(f'{cwd}/keys/token.txt', 'r') as botkey:
    token = botkey.read()

#Decalring discord bot varibles.
client = discord.Client()
client = commands.Bot(command_prefix = '$', case_insensitive=True)

#Utils functions
@client.command()
async def time(ctx):
    await ctx.send(embed=utils.timecmd())

@client.command()
async def commands(ctx):
    await ctx.send(embed=utils.helpcmd())

@client.command()
async def money(ctx):
    await ctx.send(embed=utils.moneycmd())

#Fun functions 

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


#gif functions
@client.command()
async def happybirthday (ctx):
    await ctx.send(gifs.happycmd())

@client.command()
async def rgif (ctx):
    await ctx.send(gifs.rgifcmd())

@client.command()
async def weeb (ctx):
    await ctx.send(gifs.weebcmd())
#Media functions
@client.command()
async def eurobeat (ctx):
    await ctx.send(media.eurobeatcmd())

#greeting functions
@client.command()
async def goodmorning (ctx):
    await ctx.send(greetings.goodmorningcmd())

@client.command()
async def goodafternoon (ctx):
    await ctx.send(greetings.goodafternooncmd())

@client.command()
async def goodevening (ctx):
    await ctx.send(greetings.goodeveningcmd())

@client.command()
async def goodnight (ctx):
    await ctx.send(greetings.goodnightcmd())

#web functions
@client.command()
async def rwiki (ctx):
    await ctx.send(webstuff.rwikicmd())

@client.command()
async def wikitoday (ctx):
    await ctx.send(webstuff.wikitodaycmd())

#start bot
client.run(token)

