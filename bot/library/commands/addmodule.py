from library.models.command import Command
from discord import DMChannel, TextChannel
from library.procedures.chatprocedure import ChatProcedure


class AddModule(Command):

    def __init__(self, bot):
        super().__init__("addmodule", bot)
        self.bot = bot
        self.delete_message = True
        self.allowed_sources = [DMChannel]
        self.allowed_roles = [555375267275603968,791046197300297729]


    async def on_execute(self, ctx, params):
        await ChatProcedure(self.bot).add_module(ctx)

    def __str__(self):
        return "Syntax: addmodule"
