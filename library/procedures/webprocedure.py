import asyncio
import hashlib
import os
import time
import uuid

import discord
from discord.ext import commands
from tinydb import Query, TinyDB, where
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage

from library.repositories.db import Db
from library.utilities.userhelper import UserHelper


class WebProcedure:
    modules_list = [591723123171393552, 591721912187486228, 591722865175560203, 591723051381686272, 591723086185889995,
                    591724086355558420, 591723225977978912, 591723267266445350, 591723296404406307, 591723365878988800,
                    591723388154806490, 591723418223771658, 591723436452217044, 591723479011950622, 591723509764456457,591723166594891794,
                    591723531969101824, 591723568400957461, 591723587983900692, 591723605054980107, 591723630811938816,591723663477440522,
                    591723688567504896, 591723719123140641, 591723750576357400, 591723786643046401, 591723817127116840,591723897418809368,
                    591723917689880600, 591723938657206407, 591723974094749696, 591724012728746026, 591724034857631794,591724053983789114,
                    591724086355558420, 591724139300257794, 591724192353746965, 591724222464655387, 591724252668100608,591724283550760997,624245270393389068,591653678776057882,642469055382421516] # Last ones are alumni and then teacher
    
    def __init__(self, bot):
        self.bot = bot
        self.useradmin = UserHelper(self.bot)

    async def initiate_procedure(self,user):
        db = Db()
        table = db.get_table('api_keys')
        current_hash = uuid.uuid4().hex
        table.insert({'user':user.id, 'token': current_hash, 'timeOfCreation':time.time()})
        db.db.close()
        return current_hash
        
    async def get_procedure(self, hash=None, user=None):
        db = Db()
        table = db.get_table('api_keys')
        obj = Query()
        if hash:
            obj = table.search(obj.token == hash)
            db.db.close()
            if len(obj) == 0: return False
            uid = obj[0]['user']
            time_of_creation = obj[0]['timeOfCreation']
            if time.time() - time_of_creation < 86400 :
                return uid
            else:
                await self.end_procedure(hash)
                return False
        elif user:
            obj = table.search(obj.user == user.id)
            db.db.close()
            if len(obj) == 0: return await self.initiate_procedure(user)
            
            token = obj[0]['token']
            time_of_creation = obj[0]['timeOfCreation']
            if time.time() - time_of_creation < 86400 :
                return token
            else:
                await self.end_procedure(user=user)
                return await self.initiate_procedure(user)
        
    async def end_procedure(self, hash=None, user=None):
        db = Db()
        table = db.get_table('api_keys')
        obj = Query()
        if hash:
            table.remove(obj.token == hash)

        elif user:
            table.remove(obj.user == user.id)
        
        db.db.clear_cache()
        db.db.close()
