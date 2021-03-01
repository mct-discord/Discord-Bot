from discord.ext import commands
import discord
import asyncio
from tinydb import TinyDB, Query, where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import hashlib
import time
import os
import uuid


class UserHelper:
    role_blacklist = [591659288053940272, 770937785544474624, 791046197300297729,
                      591653678776057882, 597790918736740363, 652504589463191552, 635808694554329089, 635808575108677654, 652594207051218955, 635813651554500628, 639608778655924227, 624245270393389068, 597790918736740363]

    def __init__(self, bot):
        self.bot = bot

    async def get_user(self, uid):
        return discord.utils.get(self.bot.guild.members, id=uid)

    async def add_role(self, usr, name=None, uid=None, bypass_blacklist=False):
        usr = discord.utils.get(self.bot.guild.members, id=usr.id)

        if name or uid:
            if name:
                if isinstance(name, list):
                    for role_item in name:
                        role = discord.utils.get(self.bot.guild.roles, name=role_item)
                        if role.id in self.role_blacklist and not bypass_blacklist:
                            return

                        await usr.add_roles(role_item)
                elif isinstance(name, str):
                    role = discord.utils.get(self.bot.guild.roles, name=name)
                    if role.id in self.role_blacklist and not bypass_blacklist:
                        return
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif uid:
                if isinstance(uid, list):
                    for role_item in uid:
                        role = discord.utils.get(self.bot.guild.roles, id=role_item)
                        if role.id in self.role_blacklist and not bypass_blacklist:
                            return
                        await usr.add_roles(role_item)
                elif isinstance(uid, int):
                    role = discord.utils.get(self.bot.guild.roles, id=uid)
                    if role.id in self.role_blacklist and not bypass_blacklist:
                        return
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a int for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def remove_role(self, usr, name=None, uid=None, bypass_blacklist=False):
        usr = discord.utils.get(self.bot.guild.members, id=usr.id)
        if uid:
            if isinstance(uid, list):
                for role_item in uid:
                    if role_item not in bypass_blacklist or bypass_blacklist:
                        role = discord.utils.get(self.bot.guild.roles, id=role_item)
                        await usr.remove_roles(role)
            elif isinstance(uid, int):
                if uid not in bypass_blacklist or bypass_blacklist:
                    role = discord.utils.get(self.bot.guild.roles, id=uid)
                    await usr.remove_roles(role)
            else:
                raise ValueError(
                    'When adding a role to a user use a list or a int for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def remove_roles(self, usr, name=None, uid=None, bypass_blacklist=False):
        for role in usr.roles[1:]:
            if role.id not in self.role_blacklist or bypass_blacklist:
                try:
                    await usr.remove_roles(role)
                except:
                    pass

    async def get_role(self, name=None, uid=None):
        if name or uid:
            if name:
                if isinstance(name, str):
                    return discord.utils.get(self.bot.guild.roles, name=name)
                else:
                    raise ValueError(
                        'When getting a role use a string for the name parameter.')
            elif uid:
                return discord.utils.get(self.bot.guild.roles, id=uid)

    async def get_roles(self, usr):
        usr = self.bot.guild.get_member(usr.id)
        if usr:
            return usr.roles
