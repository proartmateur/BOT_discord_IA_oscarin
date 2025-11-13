import requests
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def repetir(ctx, *, message:str):
    print (message)
    await ctx.send(message)

@bot.command()
async def weather(ctx, *, ciudad:str):
    print (ciudad)
    r = requests.get(f"http://wttr.in/{ciudad}?format=3")
    resultado = r.text
    print(resultado)
    await ctx.send(resultado)
    
    
@bot.command()
async def guardar_imagen(ctx):
    
    if ctx.message.attachments:

        for archivo in ctx.message.attachments:

            nombre_archivo = archivo.filename

            archivo_url = archivo.url

            await archivo.save(f"./{nombre_archivo}")
            await ctx.send(f"Imagen guardada como {nombre_archivo}")
        
    else:
        await ctx.send("No se encontraron imágenes para guardar.")

"""
from model import get_class

@bot.command()
async def analyze(ctx):

    if ctx.message.attachments:

        for archive in ctx.message.attachments:

            file_name = archive.filename

            file_url = archive.url

            await archive.save(f'./{file_name}')

            result = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path= file_name)

            await ctx.send(result)
        
        else:

            await ctx.send('olvidaste subirlo la imagen.')

"""
#pegar token entre comillas
token = ""
bot.run (token)