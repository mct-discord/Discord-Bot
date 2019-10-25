from threading import Thread
from library.quart import Quart, jsonify, quart_cors, request, session
from library import flow
import discord
import asyncio
import os


class API(Thread):

    def __init__(self, bot, rootpath):
        Thread.__init__(self)
        self.daemon = True
        self.bot = bot
        # Initiate API
        self.rootpath = rootpath
        self.loop = bot.loop

        self.app = Quart(__name__)
        self.app = quart_cors.cors(
            self.app, allow_origin="https://mct.funergydev.com")  # https://mctb.funergydev.com *

        self.flow = flow.Flow(self.bot)

        self.start()

    def run(self):
        @self.app.route('/api/v1/modules')
        async def modules():
            module_dict = {}

            for module in self.flow.modules_list:
                role = await self.flow.get_role(uid=module)
                module_dict[role.name] = '{}'.format(module)

            return jsonify(modules=module_dict)

        @self.app.route('/api/v1/user/<userid>')
        async def get_user(userid):
            user = discord.utils.get(
                discord.utils.get(self.bot.guilds, name='MCT').members, id=int(userid))
            return jsonify(name=user.name), 200

        @self.app.route('/api/v1/user/hash/<userid>')
        async def get_hashed_user(userid):
            uid = await self.flow.get_procedure(userid)
            if not uid:
                return jsonify(status='Hash not found'), 500
            user = discord.utils.get(
                discord.utils.get(self.bot.guilds, name='MCT').members, id=int(uid))
            return jsonify(name=user.name), 200

        @self.app.route('/api/v1/user_count')
        async def user_count():
            return jsonify(count=discord.utils.get(self.bot.guilds, name='MCT').member_count)

        @self.app.route('/api/v1/user/hash/<userid>/roles', methods=['POST', 'GET'])
        async def give_user_roles(userid):
            # Funergy: 160672936636841984
            if request.method == 'POST':
                data = await request.get_json()
                uid = await self.flow.get_procedure(userid)
                if not uid:
                    return jsonify(status='Hash not found'), 500
                user = discord.utils.get(
                    discord.utils.get(self.bot.guilds, name='MCT').members, id=int(uid))

                # # user_object = discord.utils.get(discord.utils.get(
                # #     self.bot.guilds, name='MCT').members, id=ctx.author.id)
                # # await self.remove_roles(user_object)
                await self.flow.remove_roles(user)
                for role in data['roles']:
                    await self.flow.add_role(user, uid=int(role))

                # user.give_roles(roles[0], roles[1], roles[2])
                message = await user.send('I have given you access to the modules you have requested.')
                await self.flow.end_procedure(userid)
                return jsonify(roles_given=data['roles']), 200
            elif request.method == 'GET':
                return jsonify(roles=100), 200
        # self.app.run(host="0.0.0.0", port=5000,
        #              debug=False, use_reloader=True, loop=self.loop)
        self.app.run(host="0.0.0.0", port=5000,
                     debug=False, use_reloader=True, loop=self.loop, keyfile='/etc/letsencrypt/live/mct.api.funergydev.com/privkey.pem',
                     certfile='/etc/letsencrypt/live/mct.api.funergydev.com/cert.pem')
