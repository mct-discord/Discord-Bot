from library.models.command import Command
from discord import DMChannel, TextChannel,Embed
import discord
import re

class Quote(Command):

    def __init__(self, bot):
        super().__init__("quote", bot)
        self.bot = bot
        self.delete_message = True
        self.allowed_sources = [TextChannel]

    async def on_execute(self, ctx, params):
        if len(params)==1:
            quote = await ctx.channel.fetch_message(int(params[0]))
            
            quote_embed = discord.embeds.Embed(description=quote.content)
            quote_embed.set_author(
            name=quote.author.display_name,
            icon_url=quote.author.avatar_url)

            footertext = "Quoted by %s." % (ctx.author.display_name)

            # if quote.edited_timestamp: # Message was edited
            #     post_edit_delta = quote.edited_timestamp - quote.timestamp
            #     footertext += " Edited %s later." % (
            #         await self.timedelta_timestamp_string(post_edit_delta)
            #     )

            quote_embed.set_footer(
                text=footertext,
                icon_url=ctx.author.avatar_url
            )
            quote_embed.timestamp = quote.created_at
            
            await ctx.channel.send(embed=quote_embed)
        elif len(params)==2:
            channel = discord.utils.get(
                    discord.utils.get(self.bot.guilds, name=self.bot.guildname).channels, id=int(re.sub(r"\D", "", params[0])))
            quote = await channel.fetch_message(int(params[1]))
            
            quote_embed = discord.embeds.Embed(description=quote.content)
            quote_embed.set_author(
            name=quote.author.display_name,
            icon_url=quote.author.avatar_url)

            footertext = "Quoted by {}. Originally posted in {}".format(ctx.author.display_name, channel.name)

            # if quote.edited_timestamp: # Message was edited
            #     post_edit_delta = quote.edited_timestamp - quote.timestamp
            #     footertext += " Edited %s later." % (
            #         await self.timedelta_timestamp_string(post_edit_delta)
            #     )

            quote_embed.set_footer(
                text=footertext,
                icon_url=ctx.author.avatar_url
            )
            quote_embed.timestamp = quote.created_at
            
            await ctx.channel.send(embed=quote_embed)
