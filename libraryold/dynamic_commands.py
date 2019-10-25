from discord import DMChannel, TextChannel
from discord.ext import commands
from library.models.command import Command
import discord
import asyncio
from library.flow import Flow
import re


class DynamicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.flow = Flow(bot)
        self.db = TinyDB('{}/db.json'.format(os.path.dirname(os.path.realpath(__file__))), storage=JSONStorage)
        self.table = self.db.table('dynamiccommands', cache_size=0)

    def load_custom_commands():
        obj = Query()
        obj = self.table.all()
        # for(command in obj):
        #     command_obj = Command()

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
