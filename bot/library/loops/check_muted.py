import datetime
import re

import discord
from discord import DMChannel, TextChannel
from discord.ext.tasks import loop
from tinydb import Query, TinyDB, where

from library.models.loop import Loop
from library.repositories.db import Db
from library.utilities.userhelper import UserHelper


class CheckMuted (Loop):
    
    def __init__(self, bot):
        super().__init__('CheckMuted',bot)
        self.bot = bot
    
    @loop(seconds=10)
    async def run(self):
        
        db = Db()
        table = db.get_table('muted')
        for row in table:

            timestamp = datetime.datetime.timestamp(
                datetime.datetime.now())
            if row['until'] is not None and row['until'] < timestamp:
                try:
                    obj_b = Query()
                    user = await UserHelper(self.bot).get_user(uid=row['id'])
                    if user is not None:
                        await UserHelper(self.bot).remove_role(user, uid=652504589463191552, bypass_blacklist=True)
                        print('Removing Mute of {}'.format(user.id))

                    table.remove(obj_b.id == row['id'])
                except Exception as ex:
                    print(ex)
            else:
                try:
                    user = await UserHelper(self.bot).get_user(uid=row['id'])
                    if user is not None:
                        print('Adding Mute role to {}'.format(user.id))
                        await UserHelper(self.bot).add_role(user, uid=652504589463191552, bypass_blacklist=True)
                except Exception as ex:
                    print(ex)
                

        db.db.close()
