
import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='&', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def multi(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def rest(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def split(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



@bot.command()
async def consejo(ctx):
    consejos = ["compra un termo en vez de botellas de plastico",
                "compra pilas recargables",
                "usa las latas como macetas",
                "reutiliza los trastes desechables",
                "no dejes las luces prendidas si no se usan (ademas la luz es cara y mejor ahorrar dinero)"]
    
    a = random.choice(consejos)

    
    await ctx.send(a)

@bot.command()
async def ayuda(ctx):
    await ctx.send("Comandos del bot: \n" +
                    "$add (para sumar) \n" +
                    "$rest (restar) \n" +
                    "$multi (multiplicar) \n" +
                    "$split (dividir) \n" +
                    "$meme (te da un meme) \n" +
                    "$duck (te muestra imagenes de patos) \n" +
                    "$dog (te da una imajen de un perro) \n" +
                    "$fox (te da la imajen de un zorro) \n" +
                    "$consejo (te da un consejo para que no contamines tanto)")

@bot.command()
async def meme(ctx):
    imagen = random.choice(os.listdir("imgs"))
    with open(f'imgs/{imagen}', 'rb') as f:
            picture = discord.File(f)   
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]

def get_fox_image_url():
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run('')
