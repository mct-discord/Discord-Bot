import asyncio
import re
from importlib import reload

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

import library.commands as commands
from library.commands import *
from library.models import command
from library.repositories.db import Db
from library.services import api
from library.utilities import signals


class Client(discord.Client):

    def __init__(self, guildname, rootpath):
        super().__init__()
        self.root_path = rootpath
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
        self.commands.append(chat.Chat(self))
        self.commands.append(reloadcmd.ReloadCMD(self))
        self.commands.append(test.Test(self))
        self.commands.append(quote.Quote(self))
        self.commands.append(help.Help(self))

    def load_custom_commands(self):
        db = Db()
        obj = Query()
        obj = db.get_table('commands').all()
        for cmd in obj:
            try:
                custom = _custom.Custom(
                    self, cmd['name'], cmd['type'], cmd['action'], cmd['actionValue'], cmd['returnMessage'])
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
            except:
                print("Skipped command {}".format(cmd['name']))

        db.db.close()

    async def reloadCommand(self, cmd):
        cmd_obj = next(
            (command for command in self.commands if command.name == cmd), None)
        self.commands.remove(cmd_obj)
        reload(commands)
        self.commands.append(cmd_obj)

    async def on_ready(self):
        print('Logged on as', self.user)
        self.api = api.API(self)
        signals.Signals(self, self.api)
        await self.change_presence(activity=discord.Game(name="Crunching some data"))

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

    async def on_member_join(self, member):
        await member.send(
            '**Welcome to the MCT server to get you started send me one of the following words:**\n\t- `chat` for the **chat** interface.\n\t- `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds of your time :).')
