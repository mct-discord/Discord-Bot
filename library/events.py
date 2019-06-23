from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow
import json


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as', self.bot.user)
        await self.bot.change_presence(activity=discord.Game(name="Crunching some data"))
        file = open('ranks.txt', 'w')
        for guild in self.bot.guilds:
            file.write("Roles for {}\n".format(guild.name))
            for role in guild.roles:
                if role.name == '@everyone':
                    continue
                file.write("\t- {} \t {}\n".format(role.name, role.id))
        file.close()

    # Sends DM to a new member
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(
            '**Welcome to the MCT server to get you started type in:** ```start```This will only take around 30 to 60 seconds of your time.')

    # Sends message in chat and via DM when user sends ping to any text channel in a server.
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.bot.user:
            return

        if not isinstance(message.channel, DMChannel):
            if message.content == 'ping':
                author = message.author
                await author.send('pong')
                await message.channel.send('pong')
        else:
            if message.content.lower() == 'start':
                flow = Flow(self.bot)
                await flow.start_flow(message)
