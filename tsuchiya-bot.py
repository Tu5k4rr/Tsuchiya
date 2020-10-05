#import
from datetime import datetime
from discord.ext import commands
from currency_converter import CurrencyConverter
import pytz, discord, requests, random

#declaring client
client = discord.Client()
c = CurrencyConverter()

#Read auth Token file
with open('token.txt', 'r') as file:
    token = file.read()

#set up commend prefix
client = commands.Bot(command_prefix = '!')


@client.command()
async def time(ctx):
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
    embed3 = discord.Embed(
        colour = discord.Colour.green())
    embed3.set_author(name='TimeZones')
    embed3.add_field(name='USA/West', value=f':flag_us:{f4}:', inline=False)
    embed3.add_field(name='USA/East', value=f':flag_us:{f3}', inline=False)
    embed3.add_field(name='EUROPE/UK', value=f':flag_gb:{f1}', inline=False)
    embed3.add_field(name='ASIA/Tokyo', value=f':flag_jp:{f2}', inline=False)
    await ctx.send(embed=embed3)


client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='!time', value='Returns time zones :flag_us: :flag_gb: :flag_jp:', inline=False)
    embed.add_field(name='!money', value='Returns rate of 1GBP in YEN', inline=False)
    embed.add_field(name='!randomwiki', value='Random Wikipedia Article', inline=False)
    embed.add_field(name='!wikitoday', value='Wikipedia Today Events', inline=False)
    embed.add_field(name='!roll', value='ROLL FOR DA NAT 20 SON!!', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def money(ctx):
    #GBP TO JPY
    a = c.convert(1, 'GBP', 'JPY')
    b = c.convert(100, 'GBP', 'JPY')
    c1 = c.convert(1000, 'GBP', 'JPY')
    aa = ("%.2f" % a)
    bb = ("%.2f" % b)
    cc = ("%.2f" % c1)
    #GBP TO USD
    a1 = c.convert(1, 'GBP', 'USD')
    b2 = c.convert(100, 'GBP', 'USD')
    c2 = c.convert(1000, 'GBP', 'USD')
    aa1 = ("%.2f" % a1)
    bb1 = ("%.2f" % b2)
    cc1 = ("%.2f" % c2)
    
    #emdedding
    embed1 = discord.Embed(
        colour = discord.Colour.green())
    embed1.set_author(name='£/¥')
    embed1.add_field(name='£1', value=f'¥{aa}')
    embed1.add_field(name='£100', value=f'¥{bb}')
    embed1.add_field(name='£1000', value=f'¥{cc}')
    #usd embed
    embed2 = discord.Embed(
        colour = discord.Colour.red())
    embed2.set_author(name='£/$')
    embed2.add_field(name='£1', value=f'${aa1}')
    embed2.add_field(name='£100', value=f'${bb1}')
    embed2.add_field(name='£1000', value=f'${cc1}')
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

@client.command()
async def randomwiki(ctx):
    wikiResp = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    await ctx.send(f'{wikiResp.url}')

@client.command()
async def wikitoday(ctx):
    month = datetime.now()
    mnt = month.strftime('%B')
    numday = month.strftime('%d')
    url = 'https://en.wikipedia.org/wiki/'
    await ctx.send(f'{url}{mnt}_{numday}')

@client.command()
async def roll (ctx):
    min = 1
    max = 20
    result = random.randint(min, max)
    await ctx.send(f'Rolled = {result}')


@client.command()
async def ud (ctx):
    min = 1
    max = 1000
    resid = random.randint(min, max)
    udurl = 'https://www.urbandictionary.com/random.php?page='
    await ctx.send(f'{udurl}{resid}')


client.run(token)


