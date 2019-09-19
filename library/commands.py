from discord import DMChannel, TextChannel
from discord.ext import commands
import discord
import asyncio
from library.flow import Flow
import re


class Commands(commands.Cog):
    role_whitelist = [591659288053940272,
                      555375267275603968, 591653678776057882, 597790918736740363]

    def __init__(self, bot):
        self.bot = bot
        self.flow = Flow(bot)

    # TODO: CLEANUP NEEDED
    @commands.command()
    async def setup(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send(
            '**Glad to know that you are interested in updating your roles:**\nPlease send me `chat` for the **chat** interface or `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds.')

        # await self.flow.predictive_flow(ctx)

    @commands.command()
    async def addmodule(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        await self.flow.add_module(ctx)

    @commands.command()
    async def web(self, ctx):
        token = await self.flow.get_procedure(user=ctx.author)
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send('**This is your setup url:** https://mctb.funergydev.com/?token={}'.format(token))

    @commands.command()
    async def webend(self, ctx):
        token = await self.flow.get_procedure(user=ctx.author)
        await self.flow.end_procedure(token)
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send('**Closed procedure**')

    @commands.command()
    async def international(self, ctx):
        await self.flow.add_role(ctx.author, uid=624245270393389068)
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send('**I have added you to the list of (possible) international students.**\n\t- You can converse with other students about your journey in the special channels.\n\t- Or talk about how to get an international experience within MCT.')
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
            await ctx.channel.send("This nuke everything to hell trigger is not yet active please discuss your evil ideas with the devs.")
            # members = discord.utils.get(
            #     self.bot.guilds, name='MCT').get_all_members()
            # for member in members:
            #     if member == self.bot.user:
            #         continue
            #     for role in member.roles:
            #         # if role.id == 578656111041970186:
            #         #     self.flow.add_role(
            #         #         ctx.author, uid='591653678776057882')
            #         if role.id not in self.role_whitelist:
            #             self.flow.remove_role(member, uid=role.id)

    @commands.command()
    @commands.has_role("Admin")
    async def purgechannels(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            await ctx.channel.send("This nuke everything to hell trigger is not yet active please discuss your evil ideas with the devs.")

            # channels = discord.utils.get(
            #     self.bot.guilds, name='MCT').channels
            # for channel in channels:
            #     if channel.type == 'Text' and channel.id not in self.flow.channel_whitelist:
            #         async for x in channel.history():
            #             await x.delete()
            #             await asyncio.sleep(.5)

    @commands.command()
    @commands.has_role("Admin")
    async def purgetext(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            async for x in ctx.channel.history():
                await x.delete()
                # await asyncio.sleep(.3)

    @commands.command()
    @commands.has_role("Admin")
    async def botsend(self, ctx, arg1, arg2=None):
        if not isinstance(ctx.channel, DMChannel):
            try:
                await ctx.message.delete()
            except:
                pass
            if not arg2:
                await ctx.send(arg1)
            else:
                try:
                    channel = discord.utils.get(
                        discord.utils.get(self.bot.guilds, name='MCT').channels, id=int(re.sub(r"\D", "", arg1)))
                    await channel.send(arg2)
                except:
                    await ctx.send('Unable to find the textchannel.')

    @commands.command()
    @commands.has_role("Admin")
    async def rules(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            await ctx.message.delete()
            await ctx.channel.send(content="**Rules**\n 1.\tDo not write anything purposely hurtful or mean about other students or teachers, be civil.\n 2.\tThis is an official school server, do not post any NSFW content, even though most wouldn’t mind, there are those who would rather not see this kind of content.\n 3.\tNo self-promotion ;)\n\n**Info**\n-\tTeachers only have permission to see certain channels, student privacy is respected here\n-\tWhen you join this server you should get a message from our bot, follow its instructions to receive your correct module channels.\n-\tTo update your roles as an existing user send `chat` for the chat interface or `web` for the web interface **to the MCT-Bot** in PM or type the following command anywhere in this server.\n```!setup```\n\nIf you would like to help us write this bot, pm an admin and we will get in contact.\n\nIf you would like to share this server with your classmates you can use this link: https://discord.gg/AtkVyTM")
