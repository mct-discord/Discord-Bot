from library.models.command import Command
from discord import DMChannel, TextChannel
from library.procedures.chatprocedure import ChatProcedure


class Chat(Command):

    def __init__(self, bot):
        super().__init__("chat", bot)
        self.bot = bot
        self.allowed_sources = [DMChannel]

    async def on_execute(self, ctx, params):
        await ChatProcedure(self.bot).predictive_flow(ctx)
