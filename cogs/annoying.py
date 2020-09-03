import discord
import re
from discord.ext import commands
"""
this cog is good for some servers but in general you might wanna
drop some memes and yeah have fun, and don't ping the bot it doesn't
like it that way ok
"""
class Annoying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._link_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+') # is a link? 
        
    async def delete_link(self, message):
        if not message.channel: # self explanatory
            return
        if message.author == self.bot.user: # self explanatory
            return
        if re.match(message, self._link_regex): # self explanatory do i have to tell you everything?
            try:
                await message.delete()
                await message.channel.send(f'{message.author.mention}, lol i\'m annoying right? yes that\'s my purpose you dumbass') # annoys the person even more
            except:
                pass

    async def on_message(self, message):
        await self.delete_link(message)

    async def on_message(self, message):
        if self.bot.user in message.mentions: # checks if the bot is pinged or not
            await ctx.guild.ban(ctx.author, reason="don't ping me again you fucker") # bans the fUCKING PINGER
            await ctx.send("don't worry guys nothing happend ok cool we cool right yeah cool ok cool bye now") # everything cool right guys?

def setup(bot):
    bot.add_cog(Annoying(bot)) # renamed to annoying because i had more than one idea lol
    print("gay mode activated")
