import asyncio
import inspect
import re
from importlib import import_module, reload

import discord
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

import library.commands as commands
import library.listeners as listeners
import library.loops as loops
from library.commands import *
from library.models import command, listener, loop
from library.repositories.db import Db
from library.services import api
from library.utilities import gspreadsheets, signals
from library.utilities.userhelper import UserHelper


class Client(discord.Client):

    def __init__(self, guildname, rootpath, config):
        super().__init__()
        self.root_path = rootpath
        self.commands = list()
        self.loops = list()
        self.listeners = list()
        self.command_prefix = "!"
        self.runtime_config = config

        self.spreadsheet = gspreadsheets.GSpreadsheets(
            "{}/certs/mct-discord-064e9637a331.json".format(self.root_path),config.get('logging', 'spreadsheetId'))

        self.guildname = guildname
        self.guild = self.get_guild(555371544940118016)
        self.load_commands()
        self.load_custom_commands()
        self.load_listeners()

        self.debug = False
        self.debug_commands = "botsend"
        

    def load_listeners(self):
        for cmd in listeners.__all__:
            if cmd == "_custom":
                continue

            print("Loading Listener {}".format(cmd))

            for name, obj in inspect.getmembers(import_module("library.listeners.{}".format(cmd)), inspect.isclass):
                if listener.Listener in obj.__bases__:
                    self.listeners.append(obj(self))

    def load_commands(self):
        for cmd in commands.__all__:
            if cmd == "_custom":
                continue

            print("Loading Command {}".format(cmd))

            for name, obj in inspect.getmembers(import_module("library.commands.{}".format(cmd)), inspect.isclass):
                if command.Command in obj.__bases__:
                    self.commands.append(obj(self))

    def load_custom_commands(self):
        db = Db()
        obj = Query()
        obj = db.get_table('commands').all()
        for cmd in obj:
            try:
                custom = _custom.Custom(
                    self, cmd['name'], cmd['type'], cmd['action'], cmd['actionValue'], cmd['returnMessage'])
                print("Loading Command {}".format(cmd['name']))
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
    
    async def setup_loops(self):
        for cmd in loops.__all__:
            if cmd == "_custom":
                continue

            print("Loading Loop {}".format(cmd))

            for name, obj in inspect.getmembers(import_module("library.loops.{}".format(cmd)), inspect.isclass):
                if loop.Loop in obj.__bases__:
                    instance = obj(self)
                    self.loops.append(instance)
                    instance.run.start()
                
        

    async def on_ready(self):
        print('Logged on as', self.user)
        self.api = api.API(self)
        signals.Signals(self, self.api)
        await self.change_presence(activity=discord.Game(name="Crunching some data"))
        await self.setup_loops()

    async def on_raw_reaction_add(self,reaction):
        listeners = [listener for listener in self.listeners if listener.listen_on_event == "on_raw_reaction_add"]
        
        for listener in listeners:
            try:
                await listener.execute(reaction)
            except Exception as ex:
                print(ex)
    
    async def on_raw_reaction_remove(self,reaction):
        listeners = [listener for listener in self.listeners if listener.listen_on_event == "on_raw_reaction_remove"]
        
        for listener in listeners:
            try:
                await listener.execute(reaction)
            except Exception as ex:
                print(ex)
                
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        listeners = [listener for listener in self.listeners if listener.listen_on_event == "on_message"]

        for listener in listeners:
            try:
                await listener.execute(message)
            except Exception as ex:
                print(ex)

        if message.content.startswith(self.command_prefix) or isinstance(message.channel, DMChannel):

            command_name = await command.Command.extract_command_name(message.content.lower())

            if self.debug and command_name not in self.debug_commands:
                return

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
        pass
        # await member.send(
        #    '**Welcome to the MCT server to get you started send me one of the following words:**\n\t- `chat` for the **chat** interface.\n\t- `web` for the **web** interface (Fastest).\nThis will only take a couple of seconds of your time :).')
