from discord import DMChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow


class Commands(commands.Cog):
    role_whitelist = [591659288053940272,
                      555375267275603968, 591653678776057882, 597790918736740363]

    def __init__(self, bot):
        self.bot = bot
        self.flow = Flow(bot)

    # TODO: CLEANUP NEEDED
    @commands.command()
    async def setup(self, ctx):
        flow = Flow(self.bot)
        try:
            await ctx.message.delete()
        except:
            pass
        await flow.predictive_flow(ctx)

    @commands.command()
    async def addmodule(self, ctx):
        flow = Flow(self.bot)
        try:
            await ctx.message.delete()
        except:
            pass
        await flow.add_module(ctx)

    @commands.command()
    async def web(self, ctx):
        flow = Flow(self.bot)
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send('https://mctb.funergydev.com/?token={}'.format(ctx.author.id))

    # @commands.command()
    # async def predictrole(self, ctx):
    #     flow = Flow(self.bot)
    #     await ctx.message.delete()
    #     await flow.predictive_flow(ctx)

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
                    # if role.id == 578656111041970186:
                    #     self.flow.add_role(
                    #         ctx.author, uid='591653678776057882')
                    if role.id not in self.role_whitelist:
                        self.flow.remove_role(member, uid=role.id)

    @commands.command()
    @commands.has_role("Admin")
    async def rules(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            await ctx.message.delete()
            await ctx.channel.send(content="**Rules**\n 1.\tDo not write anything purposely hurtful or mean about other students or teachers, be civil.\n 2.\tThis is an official school server, do not post any NSFW content, even though most wouldn’t mind, there are those who would rather not see this kind of content.\n\n**Info**\n-\tTeachers only have permission to see certain channels, student privacy is respected here\n-\tWhen you join this server you should get a message from our bot, follow its instructions to receive your correct module channels.\n-\tIf you would like to help us write this bot, pm an admin and we will get in contact.\n-\tTo get your roles send `start` to the MCT-Bot in PM or type the following command anywhere in this server.\n```!setup```\nIf you would like to share this server with your classmates you can use this link: https://discord.gg/AtkVyTM")
