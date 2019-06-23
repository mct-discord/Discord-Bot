from discord.ext import commands
import discord
import asyncio


class Flow:
    role_whitelist = [591659288053940272,
                      555375267275603968, 591653678776057882]
    emoji_numbers = ['1⃣', '2⃣', '3⃣', '4⃣', '6⃣', '7⃣', '8⃣', '9⃣', '0⃣']
    modules = [[[591723123171393552, 591721912187486228, 591722865175560203, 591723051381686272, 591723086185889995],
                [591724086355558420, 591723225977978912, 591723267266445350, 591723296404406307,
                    591723365878988800]],
               [[591723388154806490, 591723418223771658, 591723436452217044, 591723479011950622, 591723509764456457],
                   {'Web & App': [591723663477440522, 591723688567504896, 591723719123140641, 591723750576357400,
                                  591723630811938816],
                    'AI Engineer': [591723531969101824, 591723568400957461, 591723605054980107,
                                    591723719123140641, 591723630811938816],
                    'IoT Infrastructure': [591723587983900692, 591723786643046401, 591723817127116840,
                                           591723897418809368, 591723630811938816],
                    'Smart Tech & AI': [591723531969101824, 591723568400957461, 591723587983900692, 591723605054980107,
                                        591723630811938816]}],
               [['Stage'],
                   {'Web & App': [591723974094749696, 591724012728746026, 591724053983789114,
                                  591724086355558420,
                                  591724034857631794],
                    'AI Engineer': [591723917689880600, 591724012728746026, 591724139300257794,
                                    591724192353746965, 591724034857631794],
                    'IoT Infrastructure': [591723938657206407, 591724012728746026, 591724222464655387,
                                           591724252668100608, 591724034857631794],
                    'Smart Tech & AI': [591723917689880600, 591723938657206407, 591723974094749696,
                                        591724012728746026,
                                        591724034857631794]}]]

    def __init__(self, bot):
        self.bot = bot

    async def start_flow(self, ctx):
        channel = ctx.channel
        msg = await ctx.user.send(
            '**What year are you in?**\nIf a year is not applicable to you press the :no_entry_sign: button.')
        reactions = [self.emoji_numbers[0],
                     self.emoji_numbers[1], self.emoji_numbers[2], '🚫']

        for emoji in reactions:
            await msg.add_reaction(emoji)
            # await self.bot.add_reaction(msg, emoji)

        def check(reaction, user):
            return user == ctx.author

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            # Give first year permissions ----------------------------------------------------------------------------------
            if reaction.emoji == self.emoji_numbers[0]:
                await user.send('**I signed you up for *year 1.***')
                self.add_role(user, uid='578656098425372697')

            # Give second year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[1]:
                await user.send('**I signed you up for *year 2.***')
                self.add_role(user, uid='578656108663799818')

                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\nAlready have an idea what you\'re going to choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI\n:no_entry_sign: No Idea')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1],
                             self.emoji_numbers[2], self.emoji_numbers[3], '🚫']

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    self.add_role(user, uid='591620720875012117')
                    await user.send('**I signed you up for *2 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    self.add_role(user, uid='591621045572861962')
                    await user.send('**I signed you up for *2 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    self.add_role(user, uid='591621084110127133')
                    await user.send('**I signed you up for *2 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    self.add_role(user, uid='591620854966648832')
                    await user.send('**I signed you up for *2 Smart Tech and AI.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    await user.send('**I only signed you up for the first semester, redo the setup if you have an idea what you\'ll choose**')
                else:
                    raise Exception()

            # Give third year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[2]:
                await user.send('**I signed you up for *year 3.***')
                self.add_role(user, uid='578656111041970186')

                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1],
                             self.emoji_numbers[2], self.emoji_numbers[3]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    self.add_role(user, uid='591621299692896276')
                    await user.send('**We signed you up for *3 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    self.add_role(user, uid='591621543965097985')
                    await user.send('**We signed you up for *3 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    self.add_role(user, uid='591621593613205524')
                    await user.send('**We signed you up for *3 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    self.add_role(user, uid='591621481818095626')
                    await user.send('**We signed you up for *3 Smart Tech and AI.***')
                else:
                    raise Exception()

            await user.send('**If you are following extra modules send me this command to add them.\n```!addModule```**')

        except asyncio.TimeoutError:
            await user.send('We didn\'t get your answer try again with \n```!setup```')
        else:
            await user.send(
                'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')

    async def add_module(self, ctx):
        channel = ctx.channel

        try:
            def check(reaction, user):
                return user == ctx.author

            msg = await ctx.author.send(
                '**What year is your module in?**')
            reactions = [self.emoji_numbers[0],
                         self.emoji_numbers[1], self.emoji_numbers[2]]

            for emoji in reactions:
                await msg.add_reaction(emoji)
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            # Give first year modules ----------------------------------------------------------------------------------
            if reaction.emoji == self.emoji_numbers[0]:
                # Show options for first year
                msg = await user.send(
                    '**What semester is your module in?**\n\n:one: First semester\n:two: Second semester')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if reaction.emoji == self.emoji_numbers[0]:
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[0][0]:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                elif reaction.emoji == self.emoji_numbers[1]:
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[0][1]:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            # Give second year modules ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[1]:
                msg = await user.send(
                    '**What semester is your module in?**\n\n:one: First semester\n:two: Second semester')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if reaction.emoji == self.emoji_numbers[0]:
                    # Show options for first semester
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[1][0]:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if reaction.emoji == self.emoji_numbers[0]:
                        pass
                elif reaction.emoji == self.emoji_numbers[1]:
                    msg = await user.send(
                        '**What course is your module in?.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if reaction.emoji == self.emoji_numbers[0]:
                        # Show options for web and app
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['Web & App']:
                            role = await self.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    elif reaction.emoji == self.emoji_numbers[1]:
                        # Show options for ai engineer
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['AI Engineer']:
                            role = await self.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    elif reaction.emoji == self.emoji_numbers[2]:
                        # Show options for iot infrastructure
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['IoT Infrastructure']:
                            role = await self.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    elif reaction.emoji == self.emoji_numbers[3]:
                        # Show options for smart tech and ai
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['Smart Tech & AI']:
                            role = await self.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    else:
                        raise Exception()

            # Give third year modules ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[2]:
                msg = await user.send(
                    '**What course is your module in?.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                             self.emoji_numbers[3]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    # Show options for web and app
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[1][1]['Web & App']:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                elif reaction.emoji == self.emoji_numbers[1]:
                    # Show options for iot engineer
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[1][1]['AI Engineer']:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                elif reaction.emoji == self.emoji_numbers[2]:
                    # Show options for iot infrastructure
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[1][1]['IoT Infrastructure']:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                elif reaction.emoji == self.emoji_numbers[3]:
                    # Show options for smart tech and ai
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[1][1]['Smart Tech & AI']:
                        role = await self.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                else:
                    raise Exception()

        except asyncio.TimeoutError:
            await user.send('We couldn\'t get your answer right let\'s try this again shall we?')

        except Exception as e:
            print(e)

        else:
            await user.send(
                'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')

    async def add_role(self, usr, name=None, uid=None):
        if name or uid:
            if name:
                if isinstance(name, list):
                    for role_item in list:
                        role = discord.utils.get(
                            usr.guild.roles, name=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(name, str):
                    role = discord.utils.get(usr.guild.roles, name=name)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif uid:
                if isinstance(uid, list):
                    for role_item in list:
                        role = discord.utils.get(usr.guild.roles, id=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(uid, str):
                    role = discord.utils.get(usr.guild.roles, id=uid)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def reset_all_members(self, guild):
        members = guild.get_all_members()
        for member in members:
            if member == self.bot.user:
                continue
            for role in member.roles:
                if role.id not in self.role_whitelist:
                    self.remove_role(member, uid=role.id)

    async def remove_role(self, usr, name=None, uid=None):
        if name or uid:
            if name:
                if isinstance(name, list):
                    for role_item in list:
                        role = discord.utils.get(
                            usr.guild.roles, name=role_item)
                        await usr.remove_roles(role)
                elif isinstance(name, str):
                    role = discord.utils.get(usr.guild.roles, name=name)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif uid:
                if isinstance(uid, list):
                    for role_item in list:
                        role = discord.utils.get(usr.guild.roles, id=role_item)
                        await usr.remove_roles(role)
                elif isinstance(uid, str):
                    role = discord.utils.get(usr.guild.roles, id=uid)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def get_role(self, name=None, uid=None):
        if name or uid:
            if name:
                if isinstance(name, str):
                    pass
                    return discord.utils.get(discord.utils.get(self.bot.guilds, name='MCT').roles, name=name)
                else:
                    raise ValueError(
                        'When getting a role use a string for the name parameter.')
            elif uid:
                return discord.utils.get(discord.utils.get(self.bot.guilds, name='MCT').roles, id=uid)
