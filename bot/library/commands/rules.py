import time
import json
import re
from discord import DMChannel, TextChannel
import discord
from library.models.command import Command


class Rules(Command):

    def __init__(self, bot):
        super().__init__("rules", bot)
        self.bot = bot
        self.allowed_sources = [TextChannel]
        self.allowed_roles = [555375267275603968]

    async def on_execute(self, ctx, params):
        content = """Welcome to the official MCT server. :wave:
The following has everything you need to get started!
Have questions? Send a message to a mod or admin."""

        embed = discord.Embed(
                    title="QA", color=0x747f8d)
        
        
        value = """You don't have to worry! 
Teachers only have permission to see certain channels, student privacy is respected here"""
        embed.add_field(name=":woman_teacher: Are there teachers on this server?", value=value, inline=False)
        
        
        value = """When you join this server, after you've read the rules, you should get a message from our bot, follow its instructions to receive your correct module channels."""
        embed.add_field(name=":new: New to the server?", value=value, inline=False)
        
        
        value = """To update your roles as an existing user send `setup` to the MCT-Bot in PM or type the following command anywhere in this server.
`!setup`
"""
        embed.add_field(name=":tools: How do you change your modules?", value=value, inline=False)
        
        
        value = """If someone in MCT wants to join this server, message a mod and they will give you an invite link for that person."""
        embed.add_field(name=":call_me: What do you do when someone of MCT wants to join?", value=value, inline=False)
        
        await ctx.channel.send(content=content,embed=embed)
        
        
        embed = discord.Embed(
                    title="Rules", color=0xf04747)
        
        embed.description = "We try to enforce these rules in a fair and consistent manner. Consequences for breaking these rules are as follows:"
        
        value = """Minor infraction of the rules equals a warning."""
        embed.add_field(name=":warning:", value=value, inline=True)
        
        
        value = """After two warnings, the next infraction will result in a ban.  One major infraction also results in a ban."""
        embed.add_field(name=":stop_sign:", value=value, inline=True)
        
        value = """**Be kind and respect each other.** We're all in this together to create a welcoming community. Let's treat everyone with respect, even if you don't agree with each other's opinions. Keep it a healthy debate, not a war. This does not only apply to everyone who’s a member of this discord but is a general rule."""
        embed.add_field(name=":one:", value=value, inline=False)
        
        
        value = """**No hate speech or bullying.** Bullying of any kind isn't allowed. Any degrading comments about things like race, religion, culture, sexual orientation, gender, identity, etc. will not be tolerated. This includes swearing with the names of minority groups."""
        embed.add_field(name=":two:", value=value, inline=False)
        
        
        value = """**No NSFW**, this is an official MCT discord."""
        embed.add_field(name=":three:", value=value, inline=False)
        
        
        value = """**Respect everyone's privacy**, don't share any data without their consent, not even if you found it on a public site eg Facebook."""
        embed.add_field(name=":four:", value=value, inline=False)
        
        
        value = """**We respect the school’s regulations.** Don't discredit Howest. You can have an opinion but don't post something that is disrespectful, for example against a teacher. So anything that goes against that won't be tolerated."""
        embed.add_field(name=":five:", value=value, inline=False)
        
        
        value = """**No self-promotion and spam.**"""
        embed.add_field(name=":six:", value=value, inline=False)
        
        
        value = """**Everything you post should follow these rules.** If it's too edgy, meaning borderline against the rules it will be deleted. If your message/meme has multiple interpretations we will delete it even if you didn't mean it in that way. We want everyone to enjoy our community and your memes, so let's keep it healthy."""
        embed.add_field(name=":seven:", value=value, inline=False)
        
        
        value = """**Only post relevant messages in each text channel.** For example: in code questions, you only ask those types of questions. If the conversation shifts to a different subject, please move to the most relevant text channel. If there is no relevant text channel for your message, post it in general."""
        embed.add_field(name=":eight:", value=value, inline=False)
        
        
        value = """If you feel uncomfortable, want to talk about something or need help **you can always talk to the mods/admins**. We are here for you. We are one community."""
        embed.add_field(name=":nine:", value=value, inline=False)
        await ctx.channel.send(embed=embed)
        
        
        


        embed = discord.Embed(
                    title="Our agreement", color=0x747f8d)
        
        embed.description = "By using our server you agree to abide by the rules listed above."
        
        value = """As we are a part of MCT we also enforce Howest's regulations\n <https://www.howest.be/sites/default/files/studeren/documenten/Education-and-Examination-Regulations-2018-2019.pdf>"""
        embed.add_field(name="Howest Regulations", value=value, inline=False)
        
        value = """Upon creating a Discord account you agreed to Discord's terms of service. We'd like to remind you that these rules are also enforced on this server. <https://discordapp.com/terms>"""
        embed.add_field(name="Discord Terms of Service", value=value, inline=False)
        
        await ctx.channel.send(embed=embed)

        
        embed = discord.Embed(
                    title="Get started", color=0x44c8f5)
        embed.description = """After you've read everything, click the checkmark below this message and you'll get a message by our bot. Welcome to our server!"""
        
        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('✅')


    def __str__(self):
        return "Syntax: rules"
