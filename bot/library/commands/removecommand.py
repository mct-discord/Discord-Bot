import time
import json

from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.commands import _custom
from library.models.command import Command
from library.repositories.db import Db


class RemoveCommand(Command):

    def __init__(self, bot):
        super().__init__("removecommand", bot)
        self.bot = bot
        self.allowed_sources = [DMChannel, TextChannel]
        self.allowed_roles = [555375267275603968,791046197300297729]

    async def on_execute(self, ctx, params):
        db = Db()
        obj = Query()
        cmd_name = params[0].lower()
        db.get_table('commands').remove(obj.name == cmd_name)
        print(self.bot.commands)
        command_obj = next(
            (cmd for cmd in self.bot.commands if cmd.name == cmd_name), None)
        if command_obj:
            self.bot.commands.remove(command_obj)

    def __str__(self):
        return "Syntax: removecommand <command>"
