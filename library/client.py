import asyncio
import re

import discord
from discord import DMChannel, TextChannel
from discord.ext import commands
from tinydb import Query, TinyDB, where

from library.commands import _custom, addcommand, removecommand, web, botsend, purgetext, rules, setup, webend, addmodule
from library.models import command
from library.repositories.db import Db
from library.services import api


class Client(discord.Client):

    def __init__(self, guildname):
        super().__init__()

        self.commands = list()
        self.command_prefix = "!"

        self.guildname = guildname

        self.load_commands()
        self.load_custom_commands()

    def load_commands(self):
        self.commands.append(web.Web(self))
        self.commands.append(addcommand.AddCommand(self))
        self.commands.append(removecommand.RemoveCommand(self))
        self.commands.append(botsend.BotSend(self))
        self.commands.append(purgetext.PurgeText(self))
        self.commands.append(rules.Rules(self))
        self.commands.append(webend.WebEnd(self))
        self.commands.append(setup.Setup(self))
        self.commands.append(addmodule.AddModule(self))

    def load_custom_commands(self):
        db = Db()
        obj = Query()
        obj = db.get_table('commands').all()
        for cmd in obj:
            custom = _custom.Custom(
                self, cmd['name'], cmd['type'], cmd['action'], cmd['actionValue'])
            print("Loading {}".format(cmd['name']))
            custom.delete_message = cmd['deleteMessage']
            sources = list()
            for source in cmd['allowedSources']:
                if source.lower() == "channel.dm":
                    sources.append(DMChannel)
                elif source.lower() == "channel.text":
                    sources.append(TextChannel)

            custom.allowed_roles = cmd['allowedRoles']

            if len(sources):
                custom.allowed_sources = sources
            self.commands.append(custom)

        db.db.close()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith(self.command_prefix) or isinstance(message.channel, DMChannel):

            command_name = await command.Command.extract_command_name(message.content.lower())
            command_obj = next(
                (command for command in self.commands if command.name == command_name), None)

            if command_obj:
                print(command_name, " Called")
                try:
                    await command_obj.execute(message, message.content)
                except Exception as ex:
                    print(ex)
                    await message.channel.send(command_obj)

    async def on_ready(self):
        # Initiate the API
        self.api = api.API(self)

        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Game(name="Crunching some data"))
