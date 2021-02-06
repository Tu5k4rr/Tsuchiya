from discord.ext import commands
from datetime import datetime
import discord, requests


#Get random Wikipedia Page.
def rwikicmd():
    wikiResp = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    fwiki = wikiResp.url
    return fwiki

#Wikipedia on this day page.
def wikitodaycmd():
    month = datetime.now()
    mnt = month.strftime('%B')
    numday = month.strftime('%d')
    url = 'https://en.wikipedia.org/wiki/'
    ftwiki = (f'{url}{mnt}_{numday}')
    return ftwiki
