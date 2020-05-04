import discord
from discord.ext import commands


command_list = ["!KRANTHOS ", "!kranthos ", "!Kranthos "] 

bot = commands.Bot(command_prefix=commands.when_mentioned_or(*command_list), case_insensitive=True)

@bot.event

async def on_ready():
    print('Kranthos Bot running!')

@bot.command()

async def crazy(ctx):

    await ctx.send("Whoooaaa")

bot.run("e.i sddsf7jgsf6d5g-dhdg2hf4g4hf5gh-Yw#") #REPLACE THE TOKEN






