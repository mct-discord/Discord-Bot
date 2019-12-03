from library.models.command import Command
from discord import DMChannel, TextChannel
from library.procedures.webprocedure import WebProcedure


class Web(Command):

    def __init__(self, bot):
        super().__init__("web", bot)
        self.bot = bot
        self.delete_message = True
        self.allowed_sources = [DMChannel]

    async def on_execute(self, ctx, params):
        token = await WebProcedure(self.bot).get_procedure(user=ctx.author)
        await ctx.author.send('**This is your setup url:** https://mctdiscord.azurewebsites.net/?token={}'.format(token))

    def __str__(self):
        return "Syntax: web"
