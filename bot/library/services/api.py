from threading import Thread
from library.utilities.quart import Quart, jsonify, request, session
# from quart import Quart, jsonify, request, session
# import quart_cors
import jwt
from library.utilities import quart_cors

from library.procedures import webprocedure
from library.utilities import userhelper
import discord
import asyncio
import os
from library.services.middleware.adauth import ADAuth


class API(Thread):

    def __init__(self, bot):
        Thread.__init__(self)
        self.daemon = True
        self.bot = bot
        # Initiate API
        self.loop = bot.loop
        self.app = Quart(__name__)
        self.app = quart_cors.cors(
            self.app, allow_origin="https://mctdiscord.azurewebsites.net")  # https://mct.funergydev.com * https://mctdiscord.azurewebsites.net
        self.app.asgi_app = ADAuth(self.app.asgi_app)
        self.flow = webprocedure.WebProcedure(bot)
        self.userhelper = userhelper.UserHelper(bot)

        self.start()

    def run(self):
        @self.app.route('/api/v1/modules')
        async def modules():
            module_dict = {}

            for module in self.flow.modules_list:
                role = await self.userhelper.get_role(uid=module)
                module_dict[role.name] = '{}'.format(module)

            return jsonify(modules=module_dict)

        @self.app.route('/api/v1/invite')
        async def get_invite():
            email = jwt.decode(request.headers["authorization"].split(' ')[
                               1], verify=False)['unique_name']

            def predicate(event):
                return event.reason == 'INVITE_TO:{}'.format(email)

            channel = discord.utils.get(
                discord.utils.get(self.bot.guilds, name='MCT').channels, id=591645737779986473)
            invite = await channel.create_invite(max_age=0, max_uses=1, temporary=False, unique=True, reason='INVITE_TO:{}'.format(email))

            event = await discord.utils.get(self.bot.guilds, name='MCT').audit_logs().filter(predicate).flatten()

            if(len(event) > 1):
                action_embed = discord.embeds.Embed(title='Warning',
                                                    color=0xff8000)

                action_embed.add_field(
                    name="Description", value='User {} has created more that one invite (current: {}). He might be inviting outsiders.'.format(email, len(event)), inline=False)

                action_embed.add_field(
                    name="Invite Codes (Recents first)", value=', '.join(map(lambda x: x.changes.after.code, event)), inline=False)

                action_embed.set_author(
                    name=email)

                footertext = "Generated by MCT Bot."

                action_embed.set_footer(
                    text=footertext
                )

                channel = self.bot.get_channel(658455187547095053)

                await channel.send(embed=action_embed)

            return jsonify(invite_code=invite.code), 201

        @self.app.route('/api/v1/user/<userid>')
        async def get_user(userid):
            user = discord.utils.get(
                discord.utils.get(self.bot.guilds, name='MCT').members, id=int(userid))
            return jsonify(name=user.name), 200

        @self.app.route('/api/v1/user/hash/<userid>')
        async def get_hashed_user(userid):
            email = jwt.decode(request.headers["authorization"].split(' ')[
                               1], verify=False)['unique_name']
            
            
            uid = await self.flow.get_procedure(userid)
            if not uid:
                return jsonify(status='Hash not found'), 500
            user = discord.utils.get(
                discord.utils.get(self.bot.guilds, name='MCT').members, id=int(uid))
            
            try:
                if not user.nick or email.split('.')[0] not in user.nick.lower(): 
                    await user.edit(nick=email.split('.')[0].capitalize())
            except Exception:
                print('Forbidden on changing nicknames. User could be Owner or higher level!')
            
            return jsonify(name=user.name), 200

        @self.app.route('/api/v1/user_count')
        async def user_count():
            return jsonify(count=discord.utils.get(self.bot.guilds, name='MCT').member_count)

        @self.app.route('/api/v1/status')
        async def status():
            return jsonify(status="Operational"), 200

        @self.app.route('/api/v1/user/hash/<userid>/roles', methods=['POST', 'GET'])
        async def give_user_roles(userid):
            if request.method == 'POST':
                email = jwt.decode(request.headers["authorization"].split(' ')[
                               1], verify=False)['unique_name']
                data = await request.get_json()
                uid = await self.flow.get_procedure(userid)
                if not uid:
                    return jsonify(status='Hash not found'), 500
                user = discord.utils.get(
                    discord.utils.get(self.bot.guilds, name='MCT').members, id=int(uid))

                try:
                    if not user.nick or email.split('.')[0] not in user.nick.lower():
                        await user.edit(nick=email.split('.')[0].capitalize())
                except Exception:
                    print('Forbidden on changing nicknames. User could be Owner or higher level!')
                    
                await self.userhelper.remove_roles(user)
                for role in data['roles']:
                    if role not in self.userhelper.role_blacklist:
                        await self.userhelper.add_role(user, uid=int(role))

                await user.send('I have given you access to the modules you have requested.')
                await self.flow.end_procedure(userid)
                return jsonify(roles_given=data['roles']), 200
            elif request.method == 'GET':
                return jsonify(roles=100), 200

        # self.app.run(host="0.0.0.0", port=5000,
        #              debug=False, use_reloader=True, loop=self.loop)
        self.app.run(host="0.0.0.0", port=443,
                     debug=False, use_reloader=True, loop=self.loop, keyfile='{}/certs/privkey.pem'.format(self.bot.root_path),
                     certfile='{}/certs/cert.pem'.format(self.bot.root_path),ca_certs='{}/certs/ca.pem'.format(self.bot.root_path))
