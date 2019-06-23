from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow


class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # TODO: CLEANUP NEEDED
    @commands.command()
    async def setup(self, ctx):
        flow = Flow(self.bot)
        await flow.start_flow(ctx)

    @commands.command()
    async def addModule(self, ctx):
        flow = Flow(self.bot)
        await flow.add_module(ctx)
    
   
    @commands.command()
    async def roles(self, ctx):
        for guild in self.bot.guilds:
            roles = "Roles for {}\n".format(guild.name)
            for role in guild.roles:
                if role.name == '@everyone':
                    continue
                roles += "\t- {} \t\t\t\t\t {}\n".format(role.name, role.id)
            await ctx.channel.send(roles)

    @commands.command()
    @commands.has_role("Admin")
    async def fuck(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            author = ctx.author
            role = discord.utils.get(author.guild.roles, name='Test')
            await author.add_roles(role)
            await ctx.channel.send('Added user to the role \'Test\'')
