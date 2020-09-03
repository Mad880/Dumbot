import discord
from discord.ext import commands

initial_extensions = ['cogs.annoying']

bot = commands.Bot(command_prefix="!", description="im a bot to make you rage lmaooooooo")
bot.remove_command("help")

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

"""
not case insensitive
most used prefix
ya see what i did there
no help command, have fun
"""

@bot.event
async def on_ready():
    print("lmao hi")


@bot.command()
async def hi(ctx):
    await ctx.guild.ban(ctx.author, reason="lmao bye")
    await ctx.send("ok bye")

bot.run("nah")
