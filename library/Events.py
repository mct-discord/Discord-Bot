from discord import DMChannel
from discord.ext import commands
import discord
import asyncio


class Events(commands.Cog):
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

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as', self.bot.user)
        await self.bot.change_presence(activity=discord.Game(name="Crunching some data"))

    # Sends DM to a new member
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(
            '**Welcome to the MCT server to get you started type in:** ```start```This will only take around 30 to 60 seconds of your time.')

    # Sends message in chat and via DM when user sends ping to any text channel in a server.
    @commands.Cog.listener()
    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.bot.user:
            return

        if not isinstance(message.channel, DMChannel):
            if message.content == 'ping':
                author = message.author
                await author.send('pong')
                await message.channel.send('pong')
        else:
            if message.content.lower() == 'start':
                channel = message.channel
                msg = await channel.send(
                    '**What year are you in?**\nIf a year is not applicable to you press the :no_entry_sign: button.')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], '🚫']
                # discord.emoji.Emoji.

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                    # await self.bot.add_reaction(msg, emoji)

                def check(reaction, user):
                    # return user == ctx.author and str(reaction.emoji) == '👍'
                    return user == message.author

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == self.emoji_numbers[0]:
                        await channel.send('**We signed you up for *year 1.***'.format(reaction))
                        # Give first year permissions
                    elif reaction.emoji == self.emoji_numbers[1]:
                        # Give second year year permissions
                        msg = await channel.send(
                            '**Your year requires you to choose a sub category.**\nWhat will you choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)

                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji == self.emoji_numbers[0]:
                            await channel.send('**We signed you up for *2 Web and App.***')
                        elif reaction.emoji == self.emoji_numbers[1]:
                            await channel.send('**We signed you up for *2 AI Engineer.***')
                        elif reaction.emoji == self.emoji_numbers[2]:
                            await channel.send('**We signed you up for *2 IoT Infrastructure.***')
                        elif reaction.emoji == self.emoji_numbers[3]:
                            await channel.send('**We signed you up for *2 Smart Tech and AI.***')
                        else:
                            raise Exception()
                    elif reaction.emoji == self.emoji_numbers[2]:
                        # Give second year year permissions
                        msg = await channel.send(
                            '**Your year requires you to choose a sub category.**\nWhat will you choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2],
                                     self.emoji_numbers[3]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)

                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji == self.emoji_numbers[0]:
                            await channel.send('**We signed you up for *3 Web and App.***')
                        elif reaction.emoji == self.emoji_numbers[1]:
                            await channel.send('**We signed you up for *3 AI Engineer.***')
                        elif reaction.emoji == self.emoji_numbers[2]:
                            await channel.send('**We signed you up for *3 IoT Infrastructure.***')
                        elif reaction.emoji == self.emoji_numbers[3]:
                            await channel.send('**We signed you up for *3 Smart Tech and AI.***')
                        else:
                            raise Exception()

                    msg = await channel.send('**Do you wish to sign up for individual modules?**')
                    reactions = ['✅', '❎']

                    for emoji in reactions:
                        await msg.add_reaction(emoji)

                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == '✅':
                        msg = await channel.send(
                            '**What year is your module in?**')
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji == self.emoji_numbers[0]:
                            pass  # Show options for first year
                        elif reaction.emoji == self.emoji_numbers[1]:
                            msg = await channel.send(
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
                        elif reaction.emoji == self.emoji_numbers[2]:
                            # Give second year year permissions
                            msg = await channel.send(
                                '**Your year requires you to choose a sub category.**\nWhat will you choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
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
                    elif reaction.emoji == '❎':
                        pass
                    else:
                        raise Exception()

                    # await channel.send('You pressed {}'.format(reaction))
                except asyncio.TimeoutError:
                    await channel.send('We couldn\'t get your answer right let\'s try this again shall we?')
                else:
                    await channel.send(
                        'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')
