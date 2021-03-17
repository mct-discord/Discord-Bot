import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.listener import Listener
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper 
from library.procedures.webprocedure import WebProcedure

class RuleAgreement(Listener):

    def __init__(self, bot):
        super().__init__("rule_agreement", bot)
        self.bot = bot
        self.listen_on_event = "on_raw_reaction_add"
        self.targeted_sources = [TextChannel]

    async def on_execute(self, *args):
        ctx = args[0]
        if ctx.channel_id == 591645737779986473:
            user = await UserHelper(self.bot).get_user(ctx.user_id)
            token = await WebProcedure(self.bot).get_procedure(user=user)
            await user.send('**Welcome to the MCT server :wave:**\nHere\'s your personalized setup url: https://mctdiscord.azurewebsites.net/?token={}'.format(token))

        
