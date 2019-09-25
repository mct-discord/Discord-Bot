from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow
import json
from library.api import API
from library.signals import Signals


class Events(commands.Cog):

    def __init__(self, bot, rootpath):
        self.bot = bot
        self.rootpath = rootpath
        self.flow = Flow(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        # Initiate the API
        api = API(self.bot, self.rootpath)
        Signals(self.bot, api)

        print('Logged on as', self.bot.user)
        await self.bot.change_presence(activity=discord.Game(name="Crunching some data"))
        # print(self.bot.guilds[0].name)
        # for guild in self.bot.guilds:
        #     print(guild.name)
        # file = open('ranks.txt', 'w')
        # for guild in self.bot.guilds:
        #     file.write("Roles for {}\n".format(guild.name))
        #     for role in guild.roles:
        #         if role.name == '@everyone':
        #             continue
        #         file.write("\t- {} \t {}\n".format(role.name, role.id))
        # file.close()

    # Sends DM to a new member
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(
            '**Welcome to the MCT server to get you started send me one of the following words:**\n\t- `chat` for the **chat** interface.\n\t- `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds of your time :).')

    # Sends message in chat and via DM when user sends ping to any text channel in a server.
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.bot.user:
            return

        if not isinstance(message.channel, DMChannel):
            pass
        else:
            if message.content.lower() == 'chat':
                await self.flow.predictive_flow(message)
            if message.content.lower() == 'web':
                token = await self.flow.get_procedure(user=message.author)
                try:
                    await message.message.delete()
                except:
                    pass
                await message.author.send('**This is your setup url:** https://mct.funergydev.com/?token={}'.format(token))
            if message.content.lower() == 'international':
                await self.flow.add_role(message.author, uid=624245270393389068)
                await message.author.send('**I have added you to the list of (possible) international students.**\n\t- You can converse with other students about your journey in the special channels.\n\t- Or talk about how to get an international experience within MCT.')
