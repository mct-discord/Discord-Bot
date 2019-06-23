from discord.ext import commands, tasks


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.ping.start()  # Disabled for spam right now

    def cog_unload(self):
        self.ping.cancel()

    @tasks.loop(minutes=1)
    async def ping(self):
        members = self.bot.get_all_members()
        for member in members:
            if member == self.bot.user:
                continue
            print('sending message to {}'.format(member.name))

            await member.send('Test')