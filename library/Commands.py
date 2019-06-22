from discord import DMChannel
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            author = ctx.author
            await author.send('pong')
            await ctx.channel.send('pong')

    @commands.command()
    async def fuck(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            author = ctx.author
            await author.send('OKAY')
            await ctx.channel.send('FUCK')
