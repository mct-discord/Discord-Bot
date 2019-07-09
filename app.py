from library.events import Events
from library.commands import Commands
from library.tasks import Tasks
from library.api import API
from discord.ext import commands

import configparser
import os

# Get root path
root_path = os.path.dirname(os.path.realpath(__file__))
# Read config file
config = configparser.ConfigParser(allow_no_value=True)
config.read(os.path.abspath("{}/config.ini".format(root_path)))

# Initiate the bot
bot = commands.Bot(command_prefix='!', case_insensitive=True)

# Initiate the API
api = API(bot)

# Add bot components
bot.add_cog(Commands(bot))
bot.add_cog(Events(bot))
bot.add_cog(Tasks(bot))

# Run the bot
bot.run(config.get('discord', 'token'))
