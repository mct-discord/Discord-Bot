from discord import DMChannel, TextChannel
from library.models.command import Command
from library.utilities.userhelper import UserHelper
import discord
import re


class Kick(Command):

    def __init__(self, bot):
        super().__init__("kick", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968, 591659288053940272]

    async def on_execute(self, ctx, params):
        print(params)
        if len(params) == 2:
            try:
                user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))
                if any(elem.id in self.allowed_roles for elem in await UserHelper(self.bot).get_roles(user)):
                    await ctx.channel.send('Cannot kick a user of an even or higher rank.')
                    return

                self.bot.spreadsheet.add_kick(
                    user, params[1], ctx.author)

                embed = discord.Embed(
                    title="You've been kicked", color=0xff0000)
                embed.add_field(name="Reason", value=params[1], inline=False)

                await user.send(embed=embed)
                await user.kick(reason=params[1])

                action_embed = discord.embeds.Embed(title='Kicked user',
                                                    color=0xff0000)

                action_embed.add_field(
                    name="Reason", value=params[1], inline=False)

                action_embed.set_author(
                    name=user.name,
                    icon_url=user.avatar_url)

                footertext = "Kicked by %s." % (ctx.author.display_name)

                action_embed.set_footer(
                    text=footertext,
                    icon_url=ctx.author.avatar_url
                )

                channel = self.bot.get_channel(658455187547095053)

                await channel.send(embed=action_embed)
            except Exception as e:
                print(e)
                await ctx.channel.send('Unable to find the user.')

    def __str__(self):
        return "Syntax: kick [<@User>] <Reason>"
