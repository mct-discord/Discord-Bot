from threading import Thread
from flask import Flask
from flask import jsonify
from functools import partial
import discord


class API(Thread):

    def __init__(self, bot):
        Thread.__init__(self)
        self.daemon = True
        self.bot = bot
        # Initiate API
        self.app = Flask(__name__)
        self.start()

    def run(self):
        @self.app.route('/api/v1/user_count')
        def user_count():
            return jsonify(count=discord.utils.get(self.bot.guilds, name='MCT').member_count)

        self.app.run(host="0.0.0.0", port=5000,
                     debug=True, use_reloader=False)
