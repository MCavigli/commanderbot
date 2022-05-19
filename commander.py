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
        await message.channel.send('Howdy, pardner.')

bot.run(os.getenv('TOKEN'))
