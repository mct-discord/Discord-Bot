import time
import json
import re
from discord import DMChannel, TextChannel
import discord
from library.models.command import Command


class Rules(Command):

    def __init__(self, bot):
        super().__init__("comext", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968,791046197300297729]

    async def on_execute(self, ctx, params):
        embed = discord.Embed(
                    title=":sparkles: Community Extensions", color=0x44c8f5)
        embed.description = """You can enable the following MCT community extensions by reacting with the correct emoji."""
        
        
        embed.add_field(name=":earth_americas: MCT International", value='Connect with other internationals or gather information for your international stay!', inline=False)
        embed.add_field(name=":microphone2: MCT Representative", value='Make yourself known as a representative. Note: MCT students are able to tag this role.', inline=False)

        embed.add_field(name=":shinto_shrine: Anime and Manga", value='Talk about your favourite seasonal anime or new chapters in a manga.', inline=False)
        embed.add_field(name=":joystick: Gaming", value='Free games, free game recommendations what more do you need?', inline=False)
        embed.add_field(name=":clapper: Movies and Series", value='Talk about your favourite series, discus movie endings and reminisce about oldschool tv series.', inline=False)



        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('🌎')
        await message.add_reaction('🎙')
        await message.add_reaction('⛩')
        await message.add_reaction('🕹')
        await message.add_reaction('🎬')


    def __str__(self):
        return "Syntax: rules"
