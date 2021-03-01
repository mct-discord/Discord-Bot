import datetime
import re

import discord
from discord import DMChannel, TextChannel

from library.models.command import Command
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper


class Mute(Command):

    def __init__(self, bot):
        super().__init__("mute", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968, 591659288053940272, 770937785544474624,791046197300297729]

    async def on_execute(self, ctx, params):
        print(params)
        if len(params) == 2:
            try:
                user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))
                self.bot.spreadsheet.add_mute(
                    user, params[1], ctx.author)
                db = Db()

                db.get_table('muted').insert(
                    {
                        'id': user.id,
                        'until': None,
                        'reason': params[1],
                    }
                )
                db.db.close()

                await UserHelper(self.bot).add_role(user, uid=652504589463191552, bypass_blacklist=True)

                embed = discord.Embed(
                    title="You've been muted", color=0xff8000)
                embed.add_field(name="Reason", value=params[1], inline=False)
                embed.add_field(name="Duration",
                                value="Infinite", inline=False)

                await user.send(embed=embed)

                action_embed = discord.embeds.Embed(title='Muted user',
                                                    color=0xff8000)

                action_embed.add_field(
                    name="Reason", value=params[1], inline=False)

                action_embed.add_field(
                    name="Duration", value="Infinite", inline=False)

                action_embed.set_author(
                    name=user.name,
                    icon_url=user.avatar_url)

                footertext = "Muted by %s." % (ctx.author.display_name)

                action_embed.set_footer(
                    text=footertext,
                    icon_url=ctx.author.avatar_url
                )

                channel = self.bot.get_channel(658455187547095053)

                await channel.send(embed=action_embed)
            except Exception as ex:
                print(ex)
                await ctx.channel.send('Unable to find the user.')

        elif len(params) == 3:
            try:
                user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))

                total_seconds_list = str(params[2]).split(":")
                total_seconds = float(total_seconds_list[0])*60*60 + \
                    float(total_seconds_list[1])*60 + \
                    float(total_seconds_list[2])

                future_timestamp = datetime.datetime.timestamp(
                    datetime.datetime.now()) + total_seconds

                db = Db()

                db.get_table('muted').insert(
                    {
                        'id': user.id,
                        'until': future_timestamp,
                        'reason': params[1],
                    }
                )
                db.db.close()

                await UserHelper(self.bot).add_role(user, uid=652504589463191552, bypass_blacklist=True)

                self.bot.spreadsheet.add_mute(
                    user, params[1], ctx.author, params[2])

                embed = discord.Embed(
                    title="You've been muted", color=0xff8000)
                embed.add_field(name="Reason", value=params[1], inline=False)
                embed.add_field(name="Duration",
                                value=params[2], inline=False)

                await user.send(embed=embed)

                action_embed = discord.embeds.Embed(title='Muted user',
                                                    color=0xff8000)

                action_embed.add_field(
                    name="Reason", value=params[1], inline=False)

                action_embed.add_field(
                    name="Duration", value=params[2], inline=False)

                action_embed.set_author(
                    name=user.name,
                    icon_url=user.avatar_url)

                footertext = "Muted by %s." % (ctx.author.display_name)

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
        return "Syntax: mute [<@User>] <Reason>"
