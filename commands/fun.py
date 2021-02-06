from discord.ext import commands
from bs4 import BeautifulSoup
import discord, requests, json, random

#1d20 roll
def rollcmd():
    min = 1
    max = 20
    result = random.randint(min, max)
    return result


#Magic 8Ball
def ballcmd():
    a= ["As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."]
    b = random.choice(a)
    return b

#Rate 1 out of 10
def ratecmd():
    min = 1
    max = 10
    rating = random.randint(min, max)
    frate = (f'{rating}/10')
    return frate

#Pulls Random Urban Dict Word and meaning.
def udcmd():
    min = 1
    max = 1000
    resid = str(random.randint(min, max))
    udurl = 'https://www.urbandictionary.com/random.php?page='
    newurl = udurl + resid
    requd = requests.get(newurl)
    html1 = requd.content
    soup = BeautifulSoup(html1, "html.parser")
    udtitle = soup.find("div",attrs={"class":"def-header"}).text
    udmean = soup.find("div",attrs={"class":"meaning"}).text
    embedud = discord.Embed(
              title = f'{udtitle}', description = f'{udmean}', url = f'{newurl}', colour = discord.Colour.purple())
    return embedud
