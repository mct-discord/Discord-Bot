from discord import DMChannel, TextChannel
from library.models.command import Command
import discord
import re


class BotSend(Command):

    def __init__(self, bot):
        super().__init__("botsend", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        if not params[1]:
            await ctx.send(params[0])
        else:
            try:
                channel = discord.utils.get(
                    discord.utils.get(self.bot.guilds, name=bot.guildname).channels, id=int(re.sub(r"\D", "", params[0])))
                await channel.send(params[1])
            except:
                await ctx.send('Unable to find the textchannel.')
