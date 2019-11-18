import time
import json
import re
from discord import DMChannel, TextChannel
from library.models.command import Command


class ReloadCMD(Command):

    def __init__(self, bot):
        super().__init__("reloadcmd", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel, DMChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        await self.bot.reloadCommand(params[0])
        await ctx.channel.send("Reloaded command {}".format(params[0]))
