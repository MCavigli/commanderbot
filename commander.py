#!/usr/bin/env python3
import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Client()

@bot.event
async def on_ready():
    print('{0.user} has successfully logged in!'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Howdy, {0}.'.format(message.author.name))

    if message.content.startswith('!ping'):
        time = message.content[5:]
        await message.channel.send('@everyone raid starts in {} minutes!'.format(time))

bot.run(os.getenv('TOKEN'))
