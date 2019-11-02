import time
import json
import re
from discord import DMChannel, TextChannel
from tinydb import Query, TinyDB, where

from library.commands import _custom
from library.models.command import Command
from library.repositories.db import Db


class AddCommand(Command):

    def __init__(self, bot):
        super().__init__("addcommand", bot)
        self.bot = bot
        self.allowed_sources = [DMChannel, TextChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        db = Db()
        cmd_name = params[0].lower()
        cmd_action_type = params[1].lower()
        cmd_action = params[2].lower()
        cmd_action_value = params[3]

        nonrequired_vars = (
            'delete_message', 'allowed_roles', 'allowed_sources', 'return_message')
        true_values = (1, 'true', 'True', 'y', 'yes')

        cmd_delete_msg = self.delete_message
        cmd_allowed_roles = list()
        cmd_allowed_sources = list()
        cmd_return_message = ""
        if len(params) > 4:
            # CMD DELETE MSG FLAG
            cmd_delete_msg = params[4] in true_values if not params[4].startswith(nonrequired_vars) else next((param.split(
                '=')[1] in true_values for param in params if param.startswith(nonrequired_vars[0])), self.delete_message)

            # CMD ROLES FLAG
            raw_allowed_roles = self.get_param_value_list(
                params, 5, nonrequired_vars[1])

            for role in raw_allowed_roles:
                if role.lower() in raw_allowed_roles:
                    cmd_allowed_roles.append(int(role))

            # CMD SOURCE FLAG
            allowed_source_values = ["channel.text", "channel.dm"]

            raw_allowed_sources = self.get_param_value_list(
                params, 6, nonrequired_vars[2])
            for source in raw_allowed_sources:
                if source.lower() in allowed_source_values:
                    cmd_allowed_sources.append(source)

            # CMD RETURN MSG FLAG
            cmd_return_message = self.get_param_value(
                params, 7, nonrequired_vars[3])

        if cmd_delete_msg and cmd_action_type == "react":
            cmd_delete_msg = False

        db.get_table('commands').insert(
            {
                'name': cmd_name,
                'type': cmd_action_type,
                'action': cmd_action,
                'actionValue': cmd_action_value,
                'deleteMessage': cmd_delete_msg,
                'allowedSources': cmd_allowed_sources,
                'allowedRoles': cmd_allowed_roles,
                'returnMessage': cmd_return_message,
                'timestamp': time.time()
            }
        )
        db.db.close()

        custom = _custom.Custom(
            self.bot, cmd_name, cmd_action_type, cmd_action, cmd_action_value, cmd_return_message)
        sources = list()
        for source in cmd_allowed_sources:
            if source.lower() == "channel.dm":
                sources.append(DMChannel)
            elif source.lower() == "channel.text":
                sources.append(TextChannel)
        custom.allowed_roles = cmd_allowed_roles
        custom.delete_message = cmd_delete_msg
        if len(sources):
            custom.allowed_sources = sources

        self.bot.commands.append(custom)

    def get_param_value_list(self, params, index, key):
        result = []
        paramvalue = ""
        reg = re.compile(".*=.*")
        if len(params) > index and not reg.match(params[index]):
            paramvalue = params[index]
        else:
            tempparam = next(
                (param for param in params if param.startswith(key)), None)
            if tempparam is not None:
                paramvalue = tempparam.split('=')[1]
            else:
                return []
        splitparam = paramvalue.split(',')
        if len(splitparam) > 0:
            for role in splitparam:
                result.append(role)
        else:
            result = [paramvalue]
        return result

    def get_param_value(self, params, index, key):
        if len(params) > index and not params[index].startswith(key):
            return params[index]
        else:
            tempparam = next(
                (param for param in params if param.startswith(key)), None)
            if tempparam is not None:
                return tempparam.split('=')[1]

    def __str__(self):
        return "Syntax: addcommand <command> <actionType[role,react]> <action{role:[add | remove], react:[add]}> [delete_message=<True/False> | allowed_sources=channel.text(,channel.dm)] "
