from discord import DMChannel, TextChannel
from library.models.command import Command
import discord


class PurgeText(Command):

    def __init__(self, bot):
        super().__init__("purgetext", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        async for x in ctx.channel.history():
            await x.delete()

    def __str__(self):
        return "Syntax: purgetext <#Channel>"
