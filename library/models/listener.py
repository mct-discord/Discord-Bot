from abc import ABC, abstractmethod
from discord import DMChannel, TextChannel
from library.utilities.userhelper import UserHelper
import shlex


class Listener(ABC):

    def __init__(self, name, bot):
        self.bot = bot
        self.name = name
        self.targeted_sources = None
        self.targeted_roles = []

    async def is_targeted_source(self, source):
        return any(isinstance(source, x) for x in self.targeted_sources)

    async def is_targeted_role(self, user):
        # if any(isinstance(DMChannel, x) for x in self.allowed_sources):
        #     return True
        roles = await UserHelper(self.bot).get_roles(user)
        if self.targeted_roles == None or len(self.targeted_roles) == 0:
            return True
        else:
            return any(elem.id in self.targeted_roles for elem in roles)

    async def execute(self, ctx):
        if await self.is_targeted_source(ctx.channel) and await self.is_targeted_role(ctx.author):
            await self.on_execute(ctx)

    @abstractmethod
    async def on_execute(self, ctx):
        pass

    def __str__(self):
        return "Something went wrong with listener: {}".format(self.name)
