import discord
from discord import DMChannel
import configparser
import os


class MCTBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    # Sends DM to a new member
    async def on_member_join(self, member):
        await member.send('Hey ;)')

    # Sends 'pong' in chat and via DM when user sends 'ping' to any text channel in a server.
    # Also gives the role named Test to the sender
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        if not isinstance(message.channel, DMChannel):
            if message.content == 'ping':
                author = message.author
                await author.add_roles(discord.utils.get(author.guild.roles, name='Test'))
                await author.send('pong')
                await message.channel.send('pong')


# Get root path
root_path = os.path.dirname(os.path.realpath(__file__))

# Read config file
config = configparser.ConfigParser(allow_no_value=True)
config.read(os.path.abspath("{}/config.ini".format(root_path)))

client = MCTBot()
client.run(config.get('discord', 'token'))
