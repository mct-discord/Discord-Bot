import time
import json
import re
from discord import DMChannel, TextChannel, Embed
from library.models.command import Command


class Help(Command):

    def __init__(self, bot):
        super().__init__("help", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel,DMChannel]

    async def on_execute(self, ctx, params):
        if not len(params):
            embed = Embed(title="Help")
            help_str = ""
            for command in self.bot.commands:
                if await command.is_allowed_role(ctx.author): # and await command.is_allowed_source(ctx.channel)
                    help_str += "\n\t- {}".format(command.name)
                    # embed.add_field(name=command.name, value="\n\t- {}".format(str(command)), inline=False)


            embed.add_field(name="Commands", value=help_str, inline=False)
            embed.add_field(name="Command specific help", value="Use: help <command>", inline=False)

            await ctx.author.send(embed=embed)
        elif len(params) == 1:
            embed = Embed(title="Help")
            help_str = ""
            
            command_obj = next(
                (command for command in self.bot.commands if command.name == params[0].lower()), None)
            if command_obj == None:
                await ctx.author.send("Help for that command does not exist.")
            else:
                if await command_obj.is_allowed_role(ctx.author):
                    help_str += "\n\t- {}".format(command_obj.name)
                        # embed.add_field(name=command.name, value="\n\t- {}".format(str(command)), inline=False)
                    embed.add_field(name=command_obj.name, value=str(command_obj), inline=False)
        
                    await ctx.author.send(embed=embed)
                else:
                    await ctx.author.send("Help for that command does not exist.")

                
    def __str__(self):
        return "We're in the matrix!"
