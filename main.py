import discord
from discord.ext import commands
import urllib.request
import asyncio
from bs4 import BeautifulSoup

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

@bot.event
async def on_ready():
    while not bot.is_closed:
        html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
        soup = BeautifulSoup(html,"html.parser")
        insult_text = soup.find('h1')
        print(insult_text.text)
        await bot.send_message(discord.Object(id=CHANNEL_ID_HERE), insult_text.text)
        await asyncio.sleep(0.7) # Changes how fast the messages are being posted (Anything under 0.7 will break it)

@bot.command()
async def hi(ctx):
    await ctx.guild.ban(ctx.author, reason="lmao bye")
    await ctx.send("ok bye")

bot.run("nah")
