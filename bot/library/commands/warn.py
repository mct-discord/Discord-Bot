from discord import DMChannel, TextChannel
from library.models.command import Command
from library.utilities.userhelper import UserHelper
import discord
import re


class Warn(Command):

    def __init__(self, bot):
        super().__init__("warn", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968, 591659288053940272]

    async def on_execute(self, ctx, params):
        print(params)
        if len(params) == 2:
            try:
                user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))
                self.bot.spreadsheet.add_warning(
                    user, params[1], ctx.author)

                embed = discord.Embed(
                    title="You've been warned", color=0xff8000)
                embed.add_field(name="Reason", value=params[1], inline=False)
                await user.send(embed=embed)

                action_embed = discord.embeds.Embed(title='Warned user',
                                                    color=0xff8000)

                action_embed.add_field(
                    name="Reason", value=params[1], inline=False)

                action_embed.set_author(
                    name=user.name,
                    icon_url=user.avatar_url)

                footertext = "Warned by %s." % (ctx.author.display_name)

                action_embed.set_footer(
                    text=footertext,
                    icon_url=ctx.author.avatar_url
                )

                channel = self.bot.get_channel(658455187547095053)

                await channel.send(embed=action_embed)
            except Exception as ex:
                print(ex)
                await ctx.channel.send('Unable to find the user.')

    def __str__(self):
        return "Syntax: warn [<@User>] <Reason>"
