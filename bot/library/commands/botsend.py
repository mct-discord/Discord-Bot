from discord import DMChannel, TextChannel
from library.models.command import Command
import discord
import re
from library.utilities.userhelper import UserHelper 


class BotSend(Command):

    def __init__(self, bot):
        super().__init__("botsend", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968,791046197300297729]

    async def on_execute(self, ctx, params):
        print(params)
        if len(params) == 1:
            await ctx.channel.send(params[0])
        else:
            try:
                if '@!' in params[0]:
                    user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))
                    embed = discord.Embed(
                    title="Message from the system", color=0x0000ff)
                    embed.add_field(name="Content", value=params[1], inline=False)
                    await user.send(embed=embed)
                    
                    self.bot.spreadsheet.add_message(
                    user, params[1], ctx.author)
                    
                elif '#' in params[0]:
                    channel = discord.utils.get(
                        discord.utils.get(self.bot.guilds, name=self.bot.guildname).channels, id=int(re.sub(r"\D", "", params[0])))
                    await channel.send(params[1])
                    
            except:
                await ctx.channel.send('Unable to find the recipient.')

    def __str__(self):
        return "Syntax: botsend [<#Channel>|<@User>] <Message>"
