import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.listener import Listener
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper 

class NicknameChange(Listener):

    def __init__(self, bot):
        super().__init__("nickname_change", bot)
        self.bot = bot
        self.listen_on_event = "on_member_update"

    async def on_execute(self, *args):
        before = args[0]
        after = args[0]
        
        if before.nick != None and before.nick not in after.nick:
            await after.edit(nick=before.nick) 
        
            

        
