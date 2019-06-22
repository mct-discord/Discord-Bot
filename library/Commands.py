from discord import DMChannel
from discord.ext import commands
import discord
import asyncio


class Commands(commands.Cog):
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

    # TODO: CLEANUP NEEDED
    @commands.command()
    async def setup(self, ctx):
        channel = ctx.channel
        msg = await channel.send(
            '**What year are you in?**\nIf a year is not applicable to you press the :no_entry_sign: button.')
        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], '🚫']
        # discord.emoji.Emoji.

        for emoji in reactions:
            await msg.add_reaction(emoji)
            # await self.bot.add_reaction(msg, emoji)

        def check(reaction, user):
            # return user == ctx.author and str(reaction.emoji) == '👍'
            return user == ctx.author

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            if reaction.emoji == self.emoji_numbers[0]:
                await channel.send('**We signed you up for *year 1.***'.format(reaction))
                # Give first year permissions
            elif reaction.emoji == self.emoji_numbers[1]:
                # Give second year year permissions
                msg = await channel.send(
                    '**Your year requires you to choose a sub category.**\nWhat will you choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

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
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

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
            print(reactions)
            for emoji in reactions:
                await msg.add_reaction(emoji)

            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            if reaction.emoji == '✅':
                pass
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

    @commands.command()
    async def roles(self, ctx):
        for guild in self.bot.guilds:
            roles = "Roles for {}\n".format(guild.name)
            for role in guild.roles:
                if role.name == '@everyone':
                    continue
                roles += "\t- {}\n".format(role.name)
            await ctx.channel.send(roles)

    @commands.command()
    @commands.has_role("Admin")
    async def fuck(self, ctx):
        if not isinstance(ctx.channel, DMChannel):
            author = ctx.author
            role = discord.utils.get(author.guild.roles, name='Test')
            await author.add_roles(role)
            await ctx.channel.send('Added user to the role \'Test\'')
