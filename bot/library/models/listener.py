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
        self.listen_on_event = "on_message"

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

    async def execute(self, *args):
        if self.listen_on_event == "on_message":
            if await self.is_targeted_source(args[0].channel) and await self.is_targeted_role(args[0].author):
                await self.on_execute(args[0])
        elif self.listen_on_event in ["on_raw_reaction_add","on_raw_reaction_remove"]:
            await self.on_execute(args[0])
        elif self.listen_on_event in ["on_member_update"]:
            await self.on_execute(args[0],args[1])

    @abstractmethod
    async def on_execute(self, *args):
        pass

    def __str__(self):
        return "Something went wrong with listener: {}".format(self.name)
