import discord
from discord.ext import commands

command_list = ["#INPUT_TEXT ", "#INPUT_TEXT ", "#INPUT_TEXT "] 

bot = commands.Bot(command_prefix=commands.when_mentioned_or(*command_list), case_insensitive=True)

@bot.event
async def on_ready():
    print('bot is online!')

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

bot.run("#REPLACE_BY_TOKEN e.i sddsf7jgsf6d5g-dhdg2hf4g4hf5gh-Yw#") #REPLACE WITH YOUR TOKEN
