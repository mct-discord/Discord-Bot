import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.command import Command
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper


class Mute(Command):

    def __init__(self, bot):
        super().__init__("unmute", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968, 591659288053940272, 770937785544474624,791046197300297729]

    async def on_execute(self, ctx, params):
        print(params)
        if len(params) == 1:
            try:
                user = await UserHelper(self.bot).get_user(int(re.sub(r"\D", "", params[0])))

                db = Db()

                table = db.get_table('muted')
                obj = Query()
                table.remove(obj.id == user.id)
                await UserHelper(self.bot).remove_role(user, uid=652504589463191552)
                db.db.close()

                embed = discord.Embed(
                    title="You've been unmuted", color=0x00FF00)

                await user.send(embed=embed)

                action_embed = discord.embeds.Embed(title='Unmuted user',
                                                    color=0x00FF00)

                action_embed.set_author(
                    name=user.name,
                    icon_url=user.avatar_url)

                footertext = "Unmuted by %s." % (ctx.author.display_name)

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
        return "Syntax: unmute [<@User>]"
