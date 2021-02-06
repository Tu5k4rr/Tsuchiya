#Importing Required Libraries
from datetime import datetime
from currency_converter import CurrencyConverter
from discord.ext import commands
import discord, pytz

#TimeZones (London, Tokyo, NY and LA)
def timecmd():
    tz1 = pytz.timezone('Europe/London')
    tz2 = pytz.timezone('Asia/Tokyo')
    tz3 = pytz.timezone('America/New_York')
    tz4 = pytz.timezone('America/Los_Angeles')
    ldn_now = datetime.now(tz1)
    tky_now = datetime.now(tz2)
    nky_now = datetime.now(tz3)
    los_now = datetime.now(tz4)
    f1 = ldn_now.strftime('%H'+'h')
    f2 = tky_now.strftime('%H'+'h')
    f3 = nky_now.strftime('%H'+'h')
    f4 = los_now.strftime('%H'+'h')
    #embed
    timeEmbed = discord.Embed(
        colour = discord.Colour.green())
    timeEmbed.set_author(name='TimeZones')
    timeEmbed.add_field(name='USA/West', value=f':flag_us:{f4}:', inline=False)
    timeEmbed.add_field(name='USA/East', value=f':flag_us:{f3}', inline=False)
    timeEmbed.add_field(name='EUROPE/UK', value=f':flag_gb:{f1}', inline=False)
    timeEmbed.add_field(name='ASIA/Tokyo', value=f':flag_jp:{f2}', inline=False)
    return timeEmbed

#List commands for BOT.
def helpcmd():
    helpembed = discord.Embed(
        colour = discord.Colour.green())
    helpembed.set_author(name='Help : list of commands available')
    helpembed.add_field(name='!time', value='Returns time zones :flag_us: :flag_gb: :flag_jp:', inline=False)
    helpembed.add_field(name='!money', value='Returns rate of 1GBP in YEN', inline=False)
    helpembed.add_field(name='!rwiki', value='Random Wikipedia Article', inline=False)
    helpembed.add_field(name='!wikitoday', value='Wikipedia Today Events', inline=False)
    helpembed.add_field(name='!roll', value='ROLL FOR DA NAT 20 SON!!', inline=False)
    helpembed.add_field(name='!ud', value='Random Urban Dictonary Page', inline=False)
    helpembed.add_field(name='!ball', value='Magic Ball Will Give You All The Answers To your Questions', inline=False)
    helpembed.add_field(name='!rate', value='Rate Stuff', inline=False)
    helpembed.add_field(name='!rgif', value='Random GIF', inline=False)
    helpembed.add_field(name='!happybirthday', value='Wish HappyBirthday With a GIF', inline=False)
    helpembed.add_field(name='!goodmorning', value='Good Morning Gif', inline=False)
    helpembed.add_field(name='!goodafternoon', value='Good Afternoon Gif', inline=False)
    helpembed.add_field(name='!goodnight', value='Good Night Gif', inline=False)
    helpembed.add_field(name='!weeb', value='For the Weeb master Sander', inline=False)
    return helpembed

#Current Money GBP to whatever.
def moneycmd():
    c = CurrencyConverter()
    #GBP TO JPY
    a = c.convert(1, 'GBP', 'JPY')
    b = c.convert(100, 'GBP', 'JPY')
    c1 = c.convert(1000, 'GBP', 'JPY')
    aa = ("%.2f" % a)
    bb = ("%.2f" % b)
    cc = ("%.2f" % c1)
    #emdedding
    moneyembed = discord.Embed(
        colour = discord.Colour.green())
    moneyembed.set_author(name='£/¥')
    moneyembed.add_field(name='£1', value=f'¥{aa}')
    moneyembed.add_field(name='£100', value=f'¥{bb}')
    moneyembed.add_field(name='£1000', value=f'¥{cc}')    
    return moneyembed
