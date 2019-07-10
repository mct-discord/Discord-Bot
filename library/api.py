from threading import Thread
from library.quart import Quart, jsonify, quart_cors
import discord
import asyncio


class API(Thread):

    def __init__(self, bot):
        Thread.__init__(self)
        self.daemon = True
        self.bot = bot
        # Initiate API

        self.loop = bot.loop

        self.app = Quart(__name__)
        self.app = quart_cors.cors(self.app, allow_origin="*")
        self.start()

    def run(self):

        @self.app.route('/api/v1/user_count')
        async def user_count():
            return jsonify(count=discord.utils.get(self.bot.guilds, name='MCT').member_count)

        @self.app.route('/api/v1/give_roles/<userid>')
        async def give_user_roles(userid):
            # Funergy: 160672936636841984
            user = discord.utils.get(
                self.bot.get_all_members(), id=int(userid))

            message = await user.send('This is just a test message')

            return jsonify(status=200, user=str(user), message=str(message.content)), 200

        self.app.run(host="0.0.0.0", port=5000,
                     debug=False, use_reloader=True, loop=self.loop)
