from discord import DMChannel, TextChannel
from library.models.command import Command
import discord
import re


class PurgeText(Command):

    def __init__(self, bot):
        super().__init__("purgetext", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968,791046197300297729]

    async def on_execute(self, ctx, params):
        if len(params) == 0:
            await ctx.channel.purge(limit=10000,bulk=True)

        else:
            channel = discord.utils.get(self.bot.guild.channels, id=int(re.sub(r"\D", "", params[0])))
            await channel.purge(limit=10000,bulk=True)


    def __str__(self):
        return "Syntax: purgetext [<#Channel>]"
