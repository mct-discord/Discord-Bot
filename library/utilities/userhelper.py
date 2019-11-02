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
    role_whitelist = [591659288053940272, 555375267275603968,
                      591653678776057882, 597790918736740363]

    def __init__(self, bot):
        self.bot = bot
        self.guildname = self.bot.guildname

    async def add_role(self, usr, name=None, uid=None):
        usr = discord.utils.get(discord.utils.get(
            self.bot.guilds, name=self.guildname).members, id=usr.id)
        if name or uid:
            if name:
                if isinstance(name, list):
                    for role_item in name:
                        role = discord.utils.get(discord.utils.get(
                            self.bot.guilds, name=self.guildname).roles, name=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(name, str):
                    role = discord.utils.get(discord.utils.get(
                        self.bot.guilds, name=self.guildname).roles, name=name)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif uid:
                if isinstance(uid, list):
                    for role_item in uid:
                        role = discord.utils.get(discord.utils.get(
                            self.bot.guilds, name=self.guildname).roles, id=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(uid, int):
                    role = discord.utils.get(discord.utils.get(
                        self.bot.guilds, name=self.guildname).roles, id=uid)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a int for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def remove_role(self, usr, name=None, uid=None):
        usr = discord.utils.get(discord.utils.get(
            self.bot.guilds, name=self.guildname).members, id=usr.id)
        if name or uid:
            if name:
                if isinstance(name, list):
                    for role_item in name:
                        role = discord.utils.get(discord.utils.get(
                            self.bot.guilds, name=self.guildname).roles, name=role_item)
                        await usr.remove_roles(role)
                elif isinstance(name, str):
                    role = discord.utils.get(discord.utils.get(
                        self.bot.guilds, name=self.guildname).roles, name=name)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif uid:
                if isinstance(uid, list):
                    for role_item in uid:
                        role = discord.utils.get(discord.utils.get(
                            self.bot.guilds, name=self.guildname).roles, id=role_item)
                        await usr.remove_roles(role)
                elif isinstance(uid, int):
                    role = discord.utils.get(discord.utils.get(
                        self.bot.guilds, name=self.guildname).roles, id=uid)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a int for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def remove_roles(self, usr, name=None, uid=None):
        for role in usr.roles[1:]:
            if role.id not in self.role_whitelist:
                try:
                    await usr.remove_roles(role)
                except:
                    pass

    async def get_role(self, name=None, uid=None):
        if name or uid:
            if name:
                if isinstance(name, str):
                    return discord.utils.get(discord.utils.get(self.bot.guilds, name=self.guildname).roles, name=name)
                else:
                    raise ValueError(
                        'When getting a role use a string for the name parameter.')
            elif uid:
                return discord.utils.get(discord.utils.get(self.bot.guilds, name=self.guildname).roles, id=uid)

    async def get_roles(self, usr):
        usr = discord.utils.get(discord.utils.get(
            self.bot.guilds, name=self.guildname).members, id=usr.id)

        if usr:
            return usr.roles
