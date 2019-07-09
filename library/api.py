from threading import Thread
from library.quart import Quart, jsonify
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
        self.start()

    def run(self):

        @self.app.route('/api/v1/user_count')
        async def user_count():
            return jsonify(count=discord.utils.get(self.bot.guilds, name='MCT').member_count)

        @self.app.route('/api/v1/give_roles/<userid>')
        async def give_user_roles(userid):
            # 160672936636841984
            user = discord.utils.get(
                self.bot.get_all_members(), id=int(userid))

            message = self.loop.create_task(
                user.send('This is just a test message'))
            await asyncio.gather(message)
            # message = self.loop.run_until_complete(task)

            return jsonify(status=200, user=str(user), message=str(message.result().content)), 200

        # @self.app.route('/api/v1/send_message/<userid>')

        # self.loop.create_task(self.loop.create_server(
        #     lambda: quart.serving.Server(self.app, loop), "0.0.0.0", 5000))
        # print('Running APP')
        # self.loop.stop()

        self.app.run(host="0.0.0.0", port=5000,
                     debug=False, use_reloader=True, loop=self.loop)
        # self.loop.run_in_executor(
        #     None, self.app.run(host="0.0.0.0", port=5000,
        #                        debug=True, use_reloader=False, loop=self.loop))
