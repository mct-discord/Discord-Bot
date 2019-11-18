from discord.ext import commands
import discord
import asyncio
import hashlib
import time
import os
import uuid
from library.utilities.userhelper import UserHelper

class ChatProcedure:
    teacher = 642469055382421516
    alumni = 591653678776057882
    emoji_numbers = ['1⃣', '2⃣', '3⃣', '4⃣','5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '0⃣']
    modules = [[[591723123171393552, 591721912187486228, 591722865175560203, 591723051381686272, 591723086185889995], 
                [591724086355558420, 591723225977978912, 591723267266445350, 591723296404406307, 591723365878988800]],
               [[591723388154806490, 591723418223771658, 591723436452217044, 591723479011950622, 591723509764456457],
                   {'Web & App': [591723663477440522, 591723688567504896, 591723719123140641, 591723750576357400, 591723630811938816],
                    'AI Engineer': [591723531969101824, 591723568400957461, 591723605054980107, 591723719123140641, 591723630811938816],
                    'IoT Infrastructure': [591723587983900692, 591723786643046401, 591723817127116840, 591723897418809368, 591723630811938816],
                    'Smart Tech & AI': [591723531969101824, 591723568400957461, 591723587983900692, 591723605054980107, 591723630811938816]}],
               [['Stage'],
                   {'Web & App': [591723974094749696, 591724012728746026, 591724053983789114, 591724086355558420, 591724034857631794],
                    'AI Engineer': [591723917689880600, 591724012728746026, 591724139300257794, 591724192353746965, 591724034857631794],
                    'IoT Infrastructure': [591723938657206407, 591724012728746026, 591724222464655387, 591724252668100608, 591724034857631794],
                    'Smart Tech & AI': [591723917689880600, 591723938657206407, 591723974094749696, 591724012728746026, 591724034857631794]}]]
    years = [578656098425372697,578656108663799818,578656111041970186]
    courses = [[],
               [[],
                [591620720875012117,591621045572861962,591620854966648832,591621084110127133]],
               [591621299692896276,591621543965097985,591621481818095626,591621593613205524]]
    channel_whitelist = [578626395480129572,578626443211177994,578626471656947749,578626503416217610,578626533921390592,578627824198615042,555372625442897930,555372741012881418,555372684565807125,555372554286530581,555372796960702485,574324141402882048,578625609362571285,578625638349668384,578625680405954560,578625724303409153,578625752606441482,578629311884427274,591633159255490580,591633745375789056,591635032540446731,591635128619630603,591638200380817428,591638265711296514,591638319310569479,591638404157145110,591639810628780042,591640141999898634,591640398590377984,591635187566379010,591661514428252180,591718410576986154,591718437307416610,591718437953339394,591641156933124097,591641390778155011,591642446492860416,591642603632459787,591644057197871136,591644161837367309,591644835568549897,591645024383401984,591645307868151808,591645528555651100,591643621166415892,591661448342798376,591719611850948620,591719642620493864,591719660911722499,591640852493762571]
    def __init__(self, bot):
        self.bot = bot
        self.useradmin = UserHelper(self.bot)

    async def start_flow(self, ctx):
        user_object = discord.utils.get(discord.utils.get(
            self.bot.guilds, name=self.bot.guildname).members, id=ctx.author.id)
        await self.useradmin.remove_roles(user_object)

        print(user_object.name)

        msg = await ctx.author.send(
            '**What year are you in?**\nIf a year is not applicable to you press the :no_entry_sign: button.')
        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], '🚫']

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
                await self.useradmin.add_role(user_object, uid=578656098425372697)
                
                # classes ----------------------------------------------------------------------------------
                msg = await user.send(
                    '**What class are you in?**\n\n:one: 1MCT 1\n:two: 1MCT 2\n:three: 1MCT 3\n:four: 1MCT 4\n:five: 1MCT 5\n:six: 1MCT 6')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4],self.emoji_numbers[5]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                    
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    await self.useradmin.add_role(user_object, uid=555374881823522816)
                elif reaction.emoji == self.emoji_numbers[1]:
                    await self.useradmin.add_role(user_object, uid=555374989918863376)
                elif reaction.emoji == self.emoji_numbers[2]:
                    await self.useradmin.add_role(user_object, uid=555375032222875656)
                elif reaction.emoji == self.emoji_numbers[3]:
                    await self.useradmin.add_role(user_object, uid=555375072693714944)
                elif reaction.emoji == self.emoji_numbers[4]:
                    await self.useradmin.add_role(user_object, uid=555375105405091840)
                elif reaction.emoji == self.emoji_numbers[5]:
                    await self.useradmin.add_role(user_object, uid=555375146094034965)
                else:
                    raise Exception()
                
                await user.send('**I have placed you in your class.**')

            # Give second year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[1]:
                await user.send('**I signed you up for *year 2.***')
                await self.useradmin.add_role(user_object, uid=578656108663799818)
                
                # classes ----------------------------------------------------------------------------------
                msg = await user.send(
                    '**What class are you in?**\n\n:one: 2MCT 1\n:two: 2MCT 2\n:three: 2MCT 3')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                    
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    await self.useradmin.add_role(user_object, uid=591620333002293251)
                elif reaction.emoji == self.emoji_numbers[1]:
                    await self.useradmin.add_role(user_object, uid=591620382344216576)
                elif reaction.emoji == self.emoji_numbers[2]:
                    await self.useradmin.add_role(user_object, uid=591620431824551937)
                else:
                    raise Exception()
                
                await user.send('**I have placed you in your class.**')
                
                # course ----------------------------------------------------------------------------------
                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\nAlready have an idea what you\'re going to choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI\n:no_entry_sign: No Idea')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], '🚫']

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    await self.useradmin.add_role(user_object, uid=591620720875012117)
                    await user.send('**I signed you up for *2 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    await self.useradmin.add_role(user_object, uid=591621045572861962)
                    await user.send('**I signed you up for *2 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    await self.useradmin.add_role(user_object, uid=591621084110127133)
                    await user.send('**I signed you up for *2 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    await self.useradmin.add_role(user_object, uid=591620854966648832)
                    await user.send('**I signed you up for *2 Smart Tech and AI.***')
                elif reaction.emoji == '🚫':
                    await user.send('**I only signed you up for the first semester, redo the setup if you have an idea what you\'ll choose**')
                else:
                    raise Exception()

            # Give third year permissions ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[2]:
                await user.send('**I signed you up for *year 3.***')
                await self.useradmin.add_role(user_object, uid=578656111041970186)

                # course ----------------------------------------------------------------------------------
                msg = await user.send(
                    '**Your year requires you to choose a sub category.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    await self.useradmin.add_role(user_object, uid=591621299692896276)
                    await user.send('**We signed you up for *3 Web and App.***')
                elif reaction.emoji == self.emoji_numbers[1]:
                    await self.useradmin.add_role(user_object, uid=591621543965097985)
                    await user.send('**We signed you up for *3 AI Engineer.***')
                elif reaction.emoji == self.emoji_numbers[2]:
                    await self.useradmin.add_role(user_object, uid=591621593613205524)
                    await user.send('**We signed you up for *3 IoT Infrastructure.***')
                elif reaction.emoji == self.emoji_numbers[3]:
                    await self.useradmin.add_role(user_object, uid=591621481818095626)
                    await user.send('**We signed you up for *3 Smart Tech and AI.***')
                else:
                    raise Exception()
            elif reaction.emoji == '🚫':
                await self.add_module(ctx)
                return
            await user.send('**If you are following extra modules send me this command to add them.\n```!addModule```**')

        except asyncio.TimeoutError:
            await user_object.send('We didn\'t get your answer try again with \n```!setup```')
        else:
            await user_object.send(
                'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')
    
    async def predictive_flow(self, ctx):        
        def check(reaction, user):
                return user == ctx.author
        
        user_object = discord.utils.get(discord.utils.get(
            self.bot.guilds, name=self.bot.guildname).members, id=ctx.author.id)
        current_year = -1
        current_course = -1
        for role in user_object.roles:
            if role.id in self.years:
                current_year = self.years.index(role.id)
        
        if current_year == -1:
            await self.start_flow(ctx)
            return
        elif current_year == 0:
            next_year = current_year+1
            next_year_id = self.years[next_year]
            msg = await ctx.author.send(
                '**Based on your previous choices I have made a prediction for you.**\nDoes the following year apply to you?\n\n\t- **Year {}**'.format(next_year+1))
            reactions = ['✅', '❎']

            for emoji in reactions:
                await msg.add_reaction(emoji)


            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == '✅':
                    await self.useradmin.remove_roles(user_object)
                    await user.send('**I signed you up for *year 2.***')
                    await self.useradmin.add_role(user_object, uid=578656108663799818)
                    # classes ----------------------------------------------------------------------------------
                    msg = await user.send(
                        '**What class are you in?**\n\n:one: 2MCT 1\n:two: 2MCT 2\n:three: 2MCT 3')
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                        
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == self.emoji_numbers[0]:
                        await self.useradmin.add_role(user_object, uid=591620333002293251)
                    elif reaction.emoji == self.emoji_numbers[1]:
                        await self.useradmin.add_role(user_object, uid=591620382344216576)
                    elif reaction.emoji == self.emoji_numbers[2]:
                        await self.useradmin.add_role(user_object, uid=591620431824551937)
                    else:
                        raise Exception()
                    
                    await user.send('**I have placed you in your class.**')
                    
                    # course ----------------------------------------------------------------------------------
                    msg = await user.send(
                        '**Your year requires you to choose a sub category.**\nAlready have an idea what you\'re going to choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI\n:no_entry_sign: No Idea')
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], '🚫']

                    for emoji in reactions:
                        await msg.add_reaction(emoji)

                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == self.emoji_numbers[0]:
                        await self.useradmin.add_role(user_object, uid=591620720875012117)
                        await user.send('**I signed you up for *2 Web and App.***')
                    elif reaction.emoji == self.emoji_numbers[1]:
                        await self.useradmin.add_role(user_object, uid=591621045572861962)
                        await user.send('**I signed you up for *2 AI Engineer.***')
                    elif reaction.emoji == self.emoji_numbers[2]:
                        await self.useradmin.add_role(user_object, uid=591621084110127133)
                        await user.send('**I signed you up for *2 IoT Infrastructure.***')
                    elif reaction.emoji == self.emoji_numbers[3]:
                        await self.useradmin.add_role(user_object, uid=591620854966648832)
                        await user.send('**I signed you up for *2 Smart Tech and AI.***')
                    elif reaction.emoji == '🚫':
                        await user.send('**I only signed you up for the first semester, redo the setup if you have an idea what you\'ll choose**')
                    else:
                        raise Exception()
                else:
                    await self.start_flow(ctx)
                    return
            except asyncio.TimeoutError:
                await user_object.send('We didn\'t get your answer try again with \n```!setup```')
            else:
                await user_object.send(
                    'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')
        elif current_year == 1:
            for role in user_object.roles:
                if role.id in self.courses[1][1]:
                    current_course = self.courses[1][1].index(role.id)
            
            if current_course == -1:
                msg = await ctx.author.send(
                    '**Based on your previous choices I have made a prediction for you.**\nWould you like to choose the following?\n\n\t- **A course**')
                reactions = ['✅', '❎']

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == '✅':
                        msg = await user_object.send(
                                '**Your year requires you to choose a sub category.**\nHave an idea what you\'re going to choose?\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)

                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji == self.emoji_numbers[0]:
                            await self.useradmin.add_role(user_object, uid=591620720875012117)
                            await user_object.send('**I signed you up for *2 Web and App.***')
                        elif reaction.emoji == self.emoji_numbers[1]:
                            await self.useradmin.add_role(user_object, uid=591621045572861962)
                            await user_object.send('**I signed you up for *2 AI Engineer.***')
                        elif reaction.emoji == self.emoji_numbers[2]:
                            await self.useradmin.add_role(user_object, uid=591621084110127133)
                            await user_object.send('**I signed you up for *2 IoT Infrastructure.***')
                        elif reaction.emoji == self.emoji_numbers[3]:
                            await self.useradmin.add_role(user_object, uid=591620854966648832)
                            await user_object.send('**I signed you up for *2 Smart Tech and AI.***')
                        else:
                            raise Exception()
                    else:
                        await self.start_flow(ctx)
                        return
                except asyncio.TimeoutError:
                    await user_object.send('We didn\'t get your answer try again with \n```!setup```')
                else:
                    await user_object.send(
                        'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')
            
            else:
                next_year = current_year+1
                next_year_id = self.years[next_year]
                next_course_id = self.courses[2][current_course]            
            
                role = await self.useradmin.get_role(uid=next_course_id)
            
                msg = await ctx.author.send(
                    '**Based on your previous choices I have made a prediction for you.**\nDoes the following course in ***year {}*** apply to you?\n\n\t- **{}**'.format(next_year+1,role.name))
                reactions = ['✅', '❎']

                for emoji in reactions:
                    await msg.add_reaction(emoji)


                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji == '✅':
                        await self.useradmin.remove_roles(user_object)
                        await self.useradmin.add_role(user_object, uid=next_year_id)
                        await self.useradmin.add_role(user_object, uid=next_course_id)
                    else:
                        await self.start_flow(ctx)
                        return
                except asyncio.TimeoutError:
                    await user_object.send('We didn\'t get your answer try again with \n```!setup```')
                else:
                    await user_object.send(
                        'If you want to redo this process you can enter the following command anytime here or on the server.```!setup```')
        elif current_year == 2:
            role = await self.useradmin.get_role(uid=591653678776057882)
            
            msg = await ctx.author.send(
                '**Based on your previous choices I have made a prediction for you.**\nDoes the following status apply to you?\n\n\t- **{}**'.format(role.name))
            reactions = ['✅', '❎']

            for emoji in reactions:
                await msg.add_reaction(emoji)


            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == '✅':
                    await self.useradmin.remove_roles(user_object)
                    await self.useradmin.add_role(user_object, uid=591653678776057882)
                    await user_object.send('The bot and the developers of this bot congratulate you. **Good Job!**\n:trophy: :champagne: :confetti_ball: ')

                else:
                    await self.start_flow(ctx)
                    return
            except asyncio.TimeoutError:
                await user_object.send('We didn\'t get your answer try again with \n```!setup```')
            else:
                await user_object.send(
                    'If you want to sign up for a year, a course or a module just type the following command.```!setup```')

    async def add_module(self, ctx):
        user_object = discord.utils.get(discord.utils.get(
                    self.bot.guilds, name=self.bot.guildname).members, id=ctx.author.id)
        try:
            def check(reaction, user):
                return user == ctx.author

            msg = await ctx.author.send(
                '**What year is your module in?**')
            reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], '🚫']

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
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[0][0][self.emoji_numbers.index(reaction.emoji)])
                elif reaction.emoji == self.emoji_numbers[1]:
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[0][1]:
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[0][1][self.emoji_numbers.index(reaction.emoji)])

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
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[1][0][self.emoji_numbers.index(reaction.emoji)])
                elif reaction.emoji == self.emoji_numbers[1]:
                    msg = await user.send(
                        '**What course is your module in?.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if reaction.emoji == self.emoji_numbers[0]:
                        # Show options for web and app
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['Web & App']:
                            role = await self.useradmin.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji in self.emoji_numbers:
                            await self.useradmin.add_role(user_object,uid=self.modules[1][1]['Web & App'][self.emoji_numbers.index(reaction.emoji)])

                    elif reaction.emoji == self.emoji_numbers[1]:
                        # Show options for ai engineer
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['AI Engineer']:
                            role = await self.useradmin.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji in self.emoji_numbers:
                            await self.useradmin.add_role(user_object,uid=self.modules[1][1]['AI Engineer'][self.emoji_numbers.index(reaction.emoji)])

                    elif reaction.emoji == self.emoji_numbers[2]:
                        # Show options for iot infrastructure
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['IoT Infrastructure']:
                            role = await self.useradmin.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji in self.emoji_numbers:
                            await self.useradmin.add_role(user_object,uid=self.modules[1][1]['IoT Infrastructure'][self.emoji_numbers.index(reaction.emoji)])

                    elif reaction.emoji == self.emoji_numbers[3]:
                        # Show options for smart tech and ai
                        option_string = '**Choose your module.**'
                        i = 0
                        for module in self.modules[1][1]['Smart Tech & AI']:
                            role = await self.useradmin.get_role(uid=module)
                            option_string += '\n{} {}'.format(
                                self.emoji_numbers[i], role.name)
                            i += 1
                        msg = await user.send(option_string)
                        reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                        for emoji in reactions:
                            await msg.add_reaction(emoji)
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                        if reaction.emoji in self.emoji_numbers:
                            await self.useradmin.add_role(user_object,uid=self.modules[1][1]['Smart Tech & AI'][self.emoji_numbers.index(reaction.emoji)])

                    else:
                        raise Exception()

            # Give third year modules ----------------------------------------------------------------------------------
            elif reaction.emoji == self.emoji_numbers[2]:
                msg = await user.send(
                    '**What course is your module in?.**\n\n:one: Web and App\n:two: AI Engineer\n:three: IoT Infrastructure\n:four: Smart Tech and AI')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3]]

                for emoji in reactions:
                    await msg.add_reaction(emoji)

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.emoji == self.emoji_numbers[0]:
                    # Show options for web and app
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[2][1]['Web & App']:
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[2][1]['Web & App'][self.emoji_numbers.index(reaction.emoji)])

                elif reaction.emoji == self.emoji_numbers[1]:
                    # Show options for iot engineer
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[2][1]['AI Engineer']:
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[2][1]['AI Engineer'][self.emoji_numbers.index(reaction.emoji)])

                elif reaction.emoji == self.emoji_numbers[2]:
                    # Show options for iot infrastructure
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[2][1]['IoT Infrastructure']:
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[2][1]['IoT Infrastructure'][self.emoji_numbers.index(reaction.emoji)])

                elif reaction.emoji == self.emoji_numbers[3]:
                    # Show options for smart tech and ai
                    option_string = '**Choose your module.**'
                    i = 0
                    for module in self.modules[2][1]['Smart Tech & AI']:
                        role = await self.useradmin.get_role(uid=module)
                        option_string += '\n{} {}'.format(
                            self.emoji_numbers[i], role.name)
                        i += 1
                    msg = await user.send(option_string)
                    reactions = [self.emoji_numbers[0], self.emoji_numbers[1], self.emoji_numbers[2], self.emoji_numbers[3], self.emoji_numbers[4]]

                    for emoji in reactions:
                        await msg.add_reaction(emoji)
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    if reaction.emoji in self.emoji_numbers:
                        await self.useradmin.add_role(user_object,uid=self.modules[2][1]['Smart Tech & AI'][self.emoji_numbers.index(reaction.emoji)])

                else:
                    raise Exception()
            elif reaction.emoji == '🚫':
                msg = await user.send(
                    '**Since the role you want isn\'t a module, choose which applies to you:**\n\n:one: 👨‍🏫 Teacher\n:two: 🏆 Alumni')
                reactions = [self.emoji_numbers[0], self.emoji_numbers[1],'🚫']

                for emoji in reactions:
                    await msg.add_reaction(emoji)
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                
                if reaction.emoji == self.emoji_numbers[0]: 
                    await self.useradmin.add_role(user_object, uid=self.teacher)
                    await user.send(
                    '**I have given you the teacher role.**\nYour next step, if you haven\'t already, will be to add yourself to your respected modules.')
                elif reaction.emoji == self.emoji_numbers[1]:
                    await self.useradmin.add_role(user_object, uid=self.alumni)
                    await user.send(
                    '**I have given you the rank of alumni.**\nCongrats by the way!')

        except asyncio.TimeoutError:
            await user_object.send('\u200b\r\nWe couldn\'t get your answer right let\'s try this again shall we?')

        except Exception as e:
            print(e)

        else:
            await user_object.send(
                '\u200b\r\nIf you want to add another module you can enter the following command anytime here or on the server.```!addmodule```')
