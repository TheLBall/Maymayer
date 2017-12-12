###################################################################
# Maymayer - A Discord bot made by DreamLive Inc. (mostly Kaniel) #
# I have no life. I have no life. I have no life. I have no life. #
###################################################################

from discord.ext import commands
import discord
import asyncio
import datetime
#get rid of the following 6 lines if you don't want stuff to be logged
import logging
import sys
import os
import aiohttp
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("token.txt","r") as tokenfile:
    token = tokenfile.read().replace('\n','')
description = '''Maymayer - Hip with the kiddest discord bot created by Luki and maintained by TheLBall.'''
startup_extensions = ["cogs.general", "cogs.fun", "cogs.mod", "cogs.math"]
bot = commands.Bot(command_prefix=['meme ', 'm!'], description=description)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='m!help • https://discord.gg/GzNH2sB'.format(len(bot.servers))))
    print('Maymayer has successfully logged in.')

# THIS IS REQUIRED STUFF, DO NOT DELETE ANYTHING PAST THIS COMMENT
@bot.event
async def on_message(message):
    if message.author.id not in bot.user.id:
        if "frick".upper() in message.content.upper():
            if message.author.id == '319503910895222784':
                await bot.send_message(message.channel,"**all hail master** :pray:")
                await bot.process_commands(message)
                return
            elif message.author.id == '201745963394531328':
                await bot.send_message(message.channel,"It's everyday bro with the Disney Channel flow **or is it**")
                await bot.process_commands(message)
                return
            elif message.author.id == '304775824182083585':
                await bot.send_message(message.channel,"**But I had an antiswear!**")
                await bot.process_commands(message)
                return
            elif message.author.id == '350285525195816970':
                await bot.send_message(message.channel,"**But I had an anti-alt!**")
                await bot.process_commands(message)
                return
            await bot.send_message(message.channel,"**thi**s is a** chri**sitan :b:e**rver no :b:u**rsing. go**t it?** :ok_hand:")
    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Oops, I lost extension {}\n{}. But I had an antivirus!'.format(extension, exc))

bot.run(token)
