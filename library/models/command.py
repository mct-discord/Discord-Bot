from abc import ABC, abstractmethod
from discord import DMChannel, TextChannel
from library.utilities.userhelper import UserHelper
import shlex


class Command(ABC):

    def __init__(self, name, bot):
        self.bot = bot
        self.name = name
        self.allowed_sources = None
        self.allowed_roles = []
        self.delete_message = True

    async def get_params(self, command):

        self.params = shlex.split(command)[1:]
        return self.params

    async def is_allowed_source(self, source):
        return any(isinstance(source, x) for x in self.allowed_sources)

    async def is_allowed_role(self, user):
        # if any(isinstance(DMChannel, x) for x in self.allowed_sources):
        #     return True
        roles = await UserHelper(self.bot).get_roles(user)
        if len(self.allowed_roles) == 0 or self.allowed_roles == None:
            return True
        else:
            return any(elem.id in self.allowed_roles for elem in roles)

    async def execute(self, ctx, command):
        if await self.is_allowed_source(ctx.channel) and await self.is_allowed_role(ctx.author):
            if self.delete_message:
                try:
                    await ctx.delete()
                except:
                    pass

            await self.on_execute(ctx, await self.get_params(command))

    @abstractmethod
    async def on_execute(self, ctx, params):
        pass

    @staticmethod
    async def extract_command_name(command):
        command = command.lstrip("!")
        command_list = command.split(" ")
        return command_list[0] if len(command_list) > 1 else command

    def __str__(self):
        return "Something went wrong executing: {}".format(self.name)
