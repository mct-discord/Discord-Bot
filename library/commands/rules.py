import time
import json
import re
from discord import DMChannel, TextChannel
from library.models.command import Command


class Rules(Command):

    def __init__(self, bot):
        super().__init__("rules", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        await ctx.channel.send(content="**Rules**\n 1.\tDo not write anything purposely hurtful or mean about other students or teachers, be civil.\n 2.\tThis is an official school server, do not post any NSFW content, even though most wouldn’t mind, there are those who would rather not see this kind of content.\n 3.\tNo self-promotion ;)\n\n**Info**\n-\tTeachers only have permission to see certain channels, student privacy is respected here\n-\tWhen you join this server you should get a message from our bot, follow its instructions to receive your correct module channels.\n-\tTo update your roles as an existing user send `chat` for the chat interface or `web` for the web interface **to the MCT-Bot** in PM or type the following command anywhere in this server.\n```!setup```\n\nIf you would like to help us write this bot, pm an admin and we will get in contact.\n\nIf you would like to share this server with your classmates you can use this link: https://discord.gg/AtkVyTM")
