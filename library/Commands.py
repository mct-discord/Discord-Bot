from discord import DMChannel
from discord.ext import commands
import discord


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
    async def roles(self, ctx):
        for guild in self.bot.guilds:
            roles = "Roles for {}\n".format(guild.name)
            for role in guild.roles:
                if role.name == '@everyone':
                    continue
                roles += "\t- {}\n".format(role.name)
            await ctx.channel.send(roles)

    @commands.command()
    @commands.has_role("Admin")
    async def fuck(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            author = ctx.author
            role = discord.utils.get(author.guild.roles, name='Test')
            await author.add_roles(role)
            await ctx.channel.send('Added user to the role \'Test\'')
