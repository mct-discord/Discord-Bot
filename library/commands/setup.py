from library.models.command import Command
from discord import DMChannel, TextChannel


class Setup(Command):

    def __init__(self, bot):
        super().__init__("setup", bot)
        self.bot = bot
        self.delete_message = True
        self.allowed_sources = [DMChannel, TextChannel]

    async def on_execute(self, ctx, params):
        await ctx.author.send(
            """**Glad to know that you are interested in updating your roles:**\n
            Please send me `chat` for the **chat** interface or `web` for the **web** interface (Fastest).\n
            This will only take a couple of seconds.""")

    def __str__(self):
        return "Syntax: setup"
