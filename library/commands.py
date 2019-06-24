from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow


class Commands(commands.Cog):

    role_whitelist = [591659288053940272,
                      555375267275603968, 591653678776057882]

    def __init__(self, bot):
        self.bot = bot
        self.flow = Flow(bot)

    # TODO: CLEANUP NEEDED
    @commands.command()
    async def setup(self, ctx):
        flow = Flow(self.bot)
        await ctx.message.delete()
        await flow.start_flow(ctx)

    @commands.command()
    async def addmodule(self, ctx):
        flow = Flow(self.bot)
        await ctx.message.delete()
        await flow.add_module(ctx)

    # @commands.command()
    # async def roles(self, ctx):
    #     for guild in self.bot.guilds:
    #         roles = "Roles for {}\n".format(guild.name)
    #         for role in guild.roles:
    #             if role.name == '@everyone':
    #                 continue
    #             roles += "\t- {} \t\t\t\t\t {}\n".format(role.name, role.id)
    #         await ctx.channel.send(roles)

    # @commands.command()
    # @commands.has_role("Admin")
    # async def fuck(self, ctx):
    #     if not isinstance(ctx.channel, DMChannel):
    #         author = ctx.author
    #         role = discord.utils.get(author.guild.roles, name='Test')
    #         await author.add_roles(role)
    #         await ctx.channel.send('Added user to the role \'Test\'')

    @commands.command()
    @commands.has_role("Admin")
    async def yeetroles(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            members = discord.utils.get(
                self.bot.guilds, name='MCT').get_all_members()
            for member in members:
                if member == self.bot.user:
                    continue
                for role in member.roles:
                    if role.id == 578656111041970186:
                        self.flow.add_role(
                            ctx.author, uid='591653678776057882')
                    if role.id not in self.role_whitelist:
                        self.flow.remove_role(member, uid=role.id)

    @commands.command()
    @commands.has_role("Admin")
    async def rules(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            pass
