import discord
from discord.ext import commands

command_list = ["#INPUT_TEXT ", "#INPUT_TEXT ", "#INPUT_TEXT "] 

bot = commands.Bot(command_prefix=commands.when_mentioned_or(*command_list), case_insensitive=True)

@bot.event
async def on_ready():
    print('#INPUT_TEXT ')

@bot.command()
async def """#REPLACE_BY_TEXT""" (ctx):
    await ctx.send("#INPUT_TEXT")

bot.run("#REPLACE_BY_TOKEN e.i sddsf7jgsf6d5g-dhdg2hf4g4hf5gh-Yw#") #REPLACE WITH YOUR TOKEN
