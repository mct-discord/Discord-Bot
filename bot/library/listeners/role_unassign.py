import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.listener import Listener
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper 

class RoleUnassign(Listener):

    def __init__(self, bot):
        super().__init__("role_unassign", bot)
        self.bot = bot
        self.listen_on_event = "on_raw_reaction_remove"
        self.targeted_sources = [TextChannel]

    async def on_execute(self, ctx):
        if ctx.message_id == 727298026481385512:
            user = await UserHelper(self.bot).get_user(ctx.user_id)
            if str(ctx.emoji) == '🌎':
                await UserHelper(self.bot).remove_role(user,uid=624245270393389068)
            elif str(ctx.emoji) == '🎙':
                await UserHelper(self.bot).remove_role(user,uid=639608778655924227)
            elif str(ctx.emoji) == '⛩':
                await UserHelper(self.bot).remove_role(user,uid=635808575108677654)
            elif str(ctx.emoji) == '🕹':
                await UserHelper(self.bot).remove_role(user,uid=635808694554329089)
            elif str(ctx.emoji) == '🎬':
                await UserHelper(self.bot).remove_role(user,uid=652594207051218955)
            

        
