import datetime
import re

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.models.listener import Listener
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper 

class RuleAgreement(Listener):

    def __init__(self, bot):
        super().__init__("rule_agreement", bot)
        self.bot = bot
        self.listen_on_event = "on_raw_reaction_add"
        self.targeted_sources = [TextChannel]

    async def on_execute(self, ctx):
        if ctx.message_id == 695727996161622136:
            user = await UserHelper(self.bot).get_user(ctx.user_id)
            await user.send('**Welcome to the MCT server :wave: to get you started send me one of the following words:**\n\t- `chat` for the **chat** interface.\n\t- `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds of your time :).')

        
