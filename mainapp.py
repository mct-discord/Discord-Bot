'''discord bot created using the discord.py library'''

# pylint: disable=W0612

import random
import json
import discord
from discord.ext import commands

def initiate_bot():

    ''' Initiate bot loop '''

    with open("token.txt", "r") as readfile:
        token = readfile.read().strip()
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        '''console output on initialization'''
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

    @bot.command(pass_context=True)
    async def multiply(ctx):
        """multiplies two numbers together"""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' * ' + str(right)
        text = str(left * right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def add(ctx):
        """Adds two numbers together."""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' + ' + str(right)
        text = str(left + right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def subtract(ctx):
        """Subtract two numbers."""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' - ' + str(right)
        text = str(left - right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def exponent(ctx):
        """raises the 1st no. to the exponent of the 2nd no."""
        number = float(ctx.message.content.split()[1])
        power = float(ctx.message.content.split()[2])
        header = str(number) + ' to the power of ' + str(power)
        text = str(number ** power)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def divide(ctx):
        """divides first number by second number"""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' / ' + str(right)
        text = str(left / right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

    @bot.command()
    async def choose(*choices: str):
        """randomly chooses between multiple options"""
        header = 'Bot has randomly chosen...'
        text = random.choice(choices)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def magicball():
        '''Answer a question with a response'''

        responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]

        random_number = random.randint(0, 19)
        if random_number >= 0 and random_number <= 9:
            embed = discord.Embed(color=0x60E87B)
        elif random_number >= 10 and random_number <= 14:
            embed = discord.Embed(color=0xECE357)
        else:
            embed = discord.Embed(color=0xD55050)

        header = 'Magic ball says...'
        text = responses[random_number]

        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def coinflip():
        '''Flips a coin'''

        random_number = random.randint(1, 1000)
        if random_number >= 500:
            text = 'It comes up tails'
        else:
            text = 'It comes up heads'

        header = 'Bot has flipped a coin...'

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def rps(ctx):
        ''' Play a game of rps '''
        choice = ctx.message.content.split()[1].lower()
        options = {'rock': 1, 'paper': 2, 'scissors': 3}

        choice = options.get(choice, 0)
        bot_choice = random.randint(1, 3)

        if choice == 0:
            header = 'Error!'
            text = 'Invalid choice! Try again.'
        # 1 > 3 > 2 > 1
        elif choice == 1:
            if bot_choice == 1:
                header = 'Tie!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'You lose!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'You win!'
                text = 'Bot has chosen scissors'
        elif choice == 2:
            if bot_choice == 1:
                header = 'You win!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'Tie!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'You lose!'
                text = 'Bot has chosen scissors'
        elif choice == 3:
            if bot_choice == 1:
                header = 'You lose!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'You win!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'Tie!'
                text = 'Bot has chosen scissors'

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def repeat(*textstring: str):
        '''get the bot to repeat some input'''
        text = ' '.join(textstring)
        embed = discord.Embed()
        embed.add_field(name='Repeat', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def addquote(*textstring: str):
        '''Adds quote to list of quotes.'''
        quotes = {}
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']

        quotes['quote_list'].append(textstring)

        with open('quotes.json', 'w') as outfile:
            json.dump(quotes, outfile)

        text = "Quote added to database."
        embed = discord.Embed()
        embed.add_field(name='Add Quote', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def getquote():
        ''' Gets quote from database. '''
        text = ''
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']
            text = quote_list[random.randint(0, len(quote_list)-1)]

        text = ' '.join(text)
        embed = discord.Embed()
        embed.add_field(name='Get Quote', value=text, inline=True)
        await bot.say(embed=embed)

    bot.run(token)

def main():

    ''' Program driver '''

    initiate_bot()

if __name__ == '__main__':
    main()