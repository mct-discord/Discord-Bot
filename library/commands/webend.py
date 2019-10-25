from library.models.command import Command
from discord import DMChannel, TextChannel
from library.procedures.webprocedure import WebProcedure

class Web(Command):
    
    def __init__(self, bot):
        super().__init__("web",bot)
        self.bot = bot
        self.delete_message = True
        self.allowed_sources = [DMChannel]
        
    async def on_execute(self, ctx, params):
        webproc = WebProcedure(self.bot)
        token = await webproc.get_procedure(user=ctx.author)
        await webproc.end_procedure(token)
        await ctx.author.send('**Closed procedure**')