from discord.ext import commands
from bs4 import BeautifulSoup
import discord, requests, json, random, os

cwd = os.getcwd()

#load file
with open(f'{cwd}/resources/ball.json', 'r') as b:
    ball = json.load(b)

#1d20 roll
def rollcmd():
    min = 1
    max = 20
    result = random.randint(min, max)
    return result


#Magic 8Ball
def ballcmd():
    br = random.choice(ball)
    return br

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
    udtitle = soup.select('h1')[0].text
    ad = []
    for i in soup.find("div", {"class":"meaning my-4"}).stripped_strings:
        ad.append(i)

    udmean = (' '.join(ad))
    embedud = discord.Embed(
                title = f'{udtitle}', description = f'{udmean}', url = f'{newurl}', colour = discord.Colour.purple())
    return embedud

def coin():
    opt = ['Heads!', 'Tails!']
    flip = random.choice(opt)
    return flip
