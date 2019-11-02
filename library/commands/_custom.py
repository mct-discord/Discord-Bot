from discord import DMChannel, TextChannel

from library.models.command import Command
from library.utilities.userhelper import UserHelper


class Custom(Command):

    def __init__(self, bot, name, type, action, value):
        super().__init__(name, bot)
        self.type = type
        self.action = action
        self.action_value = value
        self.bot = bot
        self.allowed_sources = [DMChannel, TextChannel]

    async def on_execute(self, ctx, params):
        if self.type == "send":
            if self.action == "message":
                await ctx.channel.send(self.action_value)
            if self.action == "dm":
                await ctx.channel.send(self.action_value)
        if self.type == "role":
            if self.action == "add":
                await UserHelper(self.bot).add_role(ctx.author, uid=int(self.action_value))
            elif self.action == "remove":
                await UserHelper(self.bot).remove_role(ctx.author, uid=int(self.action_value))
        elif self.type == "react":
            if self.action == "add":
                for emoji in self.action_value.split(","):
                    await ctx.add_reaction(emoji)
