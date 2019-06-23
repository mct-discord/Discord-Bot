from discord.ext import commands
import discord
import asyncio


class Flow:
    role_whitelist = ['Mod', 'Admin', 'Alumni', 'Teacher']
    emoji_numbers = ['1⃣', '2⃣', '3⃣', '4⃣', '6⃣', '7⃣', '8⃣', '9⃣']
    modules = {1: [['Prototyping', 'Basic Programming', 'Computer Networks', 'Data Science', 'User Experience'],
                   ['Full Stack Web Development', 'Sensors and Interfacing', 'Data Management', 'Create 2',
                    'Project 1']],
               2: [['Device Programming', 'Security', 'IoT Cloud', 'Interaction Design', 'Project 2'],
                   {'Web and App': ['Frontend', 'Smart App Development', 'Backend Development', 'Concept Visualisation',
                                    'Project 3'],
                    'AI Engineer': ['Advanced Programming and Math', 'Big Data', 'Machine Learning',
                                    'Backend Development', 'Project 3'],
                    'IoT Infrastructure': ['Linux OS', 'Network Infrastructure', 'Virtualisation and Cloud',
                                           'Windows OS', 'Project 3'],
                    'Smart Tech and AI': ['Advanced Programming and Math', 'Big Data', 'Linux OS', 'Machine Learning',
                                          'Project 3']}],
               3: [['Stage'],
                   {'Web and App': ['Augmented and Mixed Reality', 'Fast Forward', 'Framework and Patterns',
                                    'Full Stack Development',
                                    'Project 4'],
                    'AI Engineer': ['Deep Learning', 'Fast Forward', 'Cloud Services and DevOps',
                                    'Advanced AI', 'Project 4'],
                    'IoT Infrastructure': ['IoT Devices and Robotics', 'Fast Forward', 'Cloud Services',
                                           'Network Programming', 'Project 4'],
                    'Smart Tech and AI': ['Deep Learning', 'IoT Devices and Robotics', 'Augmented and Mixed Reality',
                                          'Fast Forward',
                                          'Project 4']}]}

    def __init__(self, bot):
        self.bot = bot

    async def start_flow(self, ctx):
        channel = ctx.channel
        msg = await user.send(
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
                self.add_role(user, 'Eerstejaars')

            # Give second year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[1]:
                await user.send('**I signed you up for *year .***')
                self.add_role(user, 'Tweedejaars')

                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\nAlready have an idea what you\'re going to choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI\n:no_entry_sign: No Idea')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1],
                             self.emoji_numbers[2], self.emoji_numbers[3], '🚫']

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    self.add_role(user, '2 Web & App')
                    await user.send('**I signed you up for *2 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    self.add_role(user, '2 AI Engineer')
                    await user.send('**I signed you up for *2 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    self.add_role(user, '2 IoT Infrastructure')
                    await user.send('**I signed you up for *2 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    self.add_role(user, '2 Smart Tech & AI')
                    await user.send('**I signed you up for *2 Smart Tech and AI.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    await user.send('**I only signed you up for the first semester, redo the setup if you have an idea what you\'ll choose**')
                else:
                    raise Exception()

            # Give third year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[2]:
                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1],
                             self.emoji_numbers[2], self.emoji_numbers[3]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    self.add_role(user, '3 Web & App')
                    await user.send('**We signed you up for *3 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    self.add_role(user, '3 AI Engineer')
                    await user.send('**We signed you up for *3 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    self.add_role(user, '3 IoT Infrastructure')
                    await user.send('**We signed you up for *3 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    self.add_role(user, '3 Smart Tech & AI')
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

            msg = await user.send(
                '**What year is your module in?**')
            reactions = [self.emoji_numbers[0],
                         self.emoji_numbers[1], self.emoji_numbers[2]]

            for emoji in reactions:
                await msg.add_reaction(emoji)
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            # Give first year modules ----------------------------------------------------------------------------------
            if reaction.emoji == self.emoji_numbers[0]:
                pass  # Show options for first year

            # Give second year modules ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[1]:
                msg = await user.send(
                    '**What semester is your module in?.**\n\n:one: First semester\n:two: Second semester')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if reaction.emoji == self.emoji_numbers[0]:
                    pass  # Show options for first semester
                elif reaction.emoji == self.emoji_numbers[1]:

                    msg = await user.send(
                        '**What course is your module in?.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                 self.emoji_numbers[3]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if reaction.emoji == self.emoji_numbers[0]:
                        pass  # Show options for web and app
                    elif reaction.emoji == self.emoji_numbers[1]:
                        pass  # Show options for ai engineer
                    elif reaction.emoji == self.emoji_numbers[2]:
                        pass  # Show options for iot infrastructure
                    elif reaction.emoji == self.emoji_numbers[3]:
                        pass  # Show options for smart tech and ai
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
                    pass  # Show options for web and app
                elif reaction.emoji == self.emoji_numbers[1]:
                    pass  # Show options for ai engineer
                elif reaction.emoji == self.emoji_numbers[2]:
                    pass  # Show options for iot infrastructure
                elif reaction.emoji == self.emoji_numbers[3]:
                    pass  # Show options for smart tech and ai
                else:
                    raise Exception()

        except asyncio.TimeoutError:
            await user.send('We couldn\'t get your answer right let\'s try this again shall we?')

        except Exception as e:
            print(e)

        else:
            await user.send(
                'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')

    async def add_role(self, usr, name=None, id=None):
        if name or id:
            if name:
                if isinstance(name, list):
                    for role_item in list:
                        role = discord.utils.get(
                            usr.guild.roles, name=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(name, str):
                    role = discord.utils.get(usr.guild.roles, name=role)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif id:
                if isinstance(id, list):
                    for role_item in list:
                        role = discord.utils.get(usr.guild.roles, id=role_item)
                        await usr.add_roles(role_item)
                elif isinstance(id, str):
                    role = discord.utils.get(usr.guild.roles, id=role)
                    await usr.add_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')

    async def reset_all_members(self):
        members = self.bot.get_all_members()
        for member in members:
            if member == self.bot.user:
                continue
            for role in member.roles:
                if role.name not in self.role_whitelist:
                    self.remove_role(member, id=role.id)

    async def remove_role(self, usr, name=None, id=None):
        if name or id:
            if name:
                if isinstance(name, list):
                    for role_item in list:
                        role = discord.utils.get(
                            usr.guild.roles, name=role_item)
                        await usr.remove_roles(role)
                elif isinstance(name, str):
                    role = discord.utils.get(usr.guild.roles, name=role)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the name parameter.')
            elif id:
                if isinstance(id, list):
                    for role_item in list:
                        role = discord.utils.get(usr.guild.roles, id=role_item)
                        await usr.remove_roles(role)
                elif isinstance(id, str):
                    role = discord.utils.get(usr.guild.roles, id=role)
                    await usr.remove_roles(role)
                else:
                    raise ValueError(
                        'When adding a role to a user use a list or a string for the id parameter.')
        else:
            raise ValueError(
                'add_role function needs to have a name or a id parameter.')
