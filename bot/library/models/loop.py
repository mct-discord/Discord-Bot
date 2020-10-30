from abc import ABC, abstractmethod
from discord import DMChannel, TextChannel
from library.utilities.userhelper import UserHelper
import shlex


class Loop(ABC):

    def __init__(self, name, bot):
        self.bot = bot
        self.name = name
   
    @abstractmethod
    async def run(self):
        pass

    def __str__(self):
        return "Something went wrong with loop: {}".format(self.name)
