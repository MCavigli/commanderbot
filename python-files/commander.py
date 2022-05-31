#!/usr/bin/env python3
import discord
import os
import aiosqlite
from dotenv import load_dotenv

def main():
    '''Allows the access of the global variable which contains the authentication TOKEN'''
    load_dotenv()

    '''Assigns Client() class to bot variable'''
    bot = discord.Client()

    @bot.event
    async def on_connect():
        print('{0.user} has successfully connected!'.format(bot))

    @bot.event
    async def on_ready():
        print('{0.user} is ready!'.format(bot))

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
            print("*-------*")
            print("Author: {}".format(message.author))
            print("Roles: {}".format(message.author.roles[1]))
            print("*-------*")

        '''Terminates program and should take the bot offline, but bot stays online a bit after'''
        if message.content.startswith('!bye'):
            print("Bot signing off")
            print("....\n...\n..\n.")
            await message.channel.send('Signing off!')
            await bot.close()

    '''Boots up the Discord bot'''
    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()
