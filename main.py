import random
import discord
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='¡', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("Hola"):
        await message.channel.send("Hola, mi nombre es bot de calentamiento global y estoy aqui para resolver dudas sobre calentamiento global, meteolrologia y mucho mas. Puedes hacer preguntas como:")

        await message.channel.send("Que es el calentamiento global")

        await message.channel.send("Que son los gases de efecto Invernadero")

        await message.channel.send("Como salvaguardar el planeta")

        await message.channel.send("Cual es el indice de calentamiento global en 2025")

        await message.channel.send("Cual ha sido el aumento de calentamiento global a lo largo de los años")

        await message.channel.send("Cual es el indice de calentamiento global en mi pais")
    

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
