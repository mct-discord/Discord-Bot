from library.models.command import Command
from library.flow import Flow


class Web(Command):
    
    def __init__(self, bot):
        super("web")
        self.bot = bot
        self.flow = Flow(bot)
        
    async def to_execute(self, ctx):
        token = await self.flow.get_procedure(user=ctx.author)
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.author.send('**This is your setup url:** https://mct.funergydev.com/?token={}'.format(token))