import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.listener import Listener
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper


class Muted(Listener):

    def __init__(self, bot):
        super().__init__("muted", bot)
        self.bot = bot
        self.targeted_sources = [TextChannel]
        self.targeted_roles = [652504589463191552]

    async def on_execute(self, ctx):
        db = Db()
        table = db.get_table('muted')
        obj = Query()
        obj = table.search(obj.id == ctx.author.id)

        if len(obj) == 0:
            await UserHelper(self.bot).remove_role(ctx.author, uid=652504589463191552)
            return

        for mute in obj:
            timestamp = datetime.datetime.timestamp(
                datetime.datetime.now())
            if mute['until'] is not None and mute['until'] < timestamp:
                obj_b = Query()
                table.remove(obj_b.id == ctx.author.id)
                await UserHelper(self.bot).remove_role(ctx.author, uid=652504589463191552)
            else:
                try:
                    await ctx.delete()
                except:
                    pass

        db.db.close()
