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
            '**Welcome to the MCT server to get you started type in:** `chat` for the **chat** interface and `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds.')

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
                flow = Flow(self.bot)
                await flow.predictive_flow(message)
            if message.content.lower() == 'web':
                token = await self.flow.get_procedure(user=ctx.author)
                try:
                    await ctx.message.delete()
                except:
                    pass
                await message.author.send('**This is your setup url:** https://mctb.funergydev.com/?token={}'.format(token))
