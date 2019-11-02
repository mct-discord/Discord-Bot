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
        print(params)
        if len(params) == 1:
            await ctx.channel.send(params[0])
        else:
            try:
                channel = discord.utils.get(
                    discord.utils.get(self.bot.guilds, name=self.bot.guildname).channels, id=int(re.sub(r"\D", "", params[0])))
                await channel.send(params[1])
            except:
                await ctx.channel.send('Unable to find the textchannel.')
