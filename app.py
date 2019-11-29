from library.client import Client

import configparser
import os
import asyncio
# Get root path
root_path = os.path.dirname(os.path.realpath(__file__))
# Read config file
config = configparser.ConfigParser(allow_no_value=True)
config.read(os.path.abspath("{}/config.ini".format(root_path)))

guildname = config.get('discord', 'guild')

# Initiate the bot
bot = Client(guildname,root_path)

# Run the bot
bot.run(config.get('discord', 'token'))
    