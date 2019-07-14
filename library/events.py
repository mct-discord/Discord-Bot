from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow
import json
from library.api import API


class Events(commands.Cog):

    def __init__(self, bot, rootpath):
        self.bot = bot
        self.rootpath = rootpath

    @commands.Cog.listener()
    async def on_ready(self):
        # Initiate the API
        api = API(self.bot, rootpath)

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
            '**Welcome to the MCT server to get you started type in:** `start` This will only take a couple of seconds.')

    # Sends message in chat and via DM when user sends ping to any text channel in a server.
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.bot.user:
            return

        if not isinstance(message.channel, DMChannel):
            pass
        else:
            if message.content.lower() == 'start':
                flow = Flow(self.bot)
                await flow.predictive_flow(message)
