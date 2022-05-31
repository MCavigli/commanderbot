#!/usr/bin/env python3
import discord
import os
from dotenv import load_dotenv

def main():
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
            if len(message.content) == 5:
                await message.channel.send('@everyone raid starts soon!')
            else:
                time = message.content[5:]
                await message.channel.send('@everyone raid starts in {} minutes!'.format(time))

        if message.content.startswith('!create'):
#        print(message.member.guild_permissions)
            print(message.author.roles)

    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()
    
