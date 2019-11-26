import time
import json
import re
from discord import DMChannel, TextChannel
from library.models.command import Command


class Test(Command):

    def __init__(self, bot):
        super().__init__("test", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = []

    async def on_execute(self, ctx, params):
        await ctx.channel.send("It works!")

    def __str__(self):
        return "Syntax: test"
