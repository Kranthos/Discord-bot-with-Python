###Lessons
#1. as we have mentioned previously, a command is composed of two parts:
#prefix
#command_name
# and we will be making both of them case insensitive (accepting A (uppercase) and a (lowercase) as the same)
#for this, we will need an array for prefixes
#basically, !kranthos will have different prefixes in command_list to make it possible to call !kranthos as an insensitive prefix

#!kranthos has "!" + "kranthos" and the issue that we have with case sensitive is with "kranthos"
#in order to get the number of all the possibilities, we will use this formula

# number_of_possibilities = 2^(number_of_letters)
#number of letters = 8.

#number of possibilities = 2^8
#number_of_possibilities = 256 (big brain calculator)

#so, we will not use all these possibilities, but we will only use three of them which are:
# KRANTHOS - Kranthos - kranthos

#let's type them in command_list=[]
#####Done

#######################################################################
#2. Now, we will define the bot command prefix
#commands.Bots(command_prefix($)) this is the syntax of this command
#we will replace command_prefix($) by our command prefix which is !kranthos in this example
#but we wanted to make it include more than !kranthos. We want it to include: !kranthos - !KRANTHOS and !Kranthos
#we stored all of the three of them in an "array" but command_prefix($) accepts "one single str"

#the solution for this is to use the following command
#commands.when_mentioned_or(*) we will input command_list and the former will unpack command_list
#let's try it out
#perfect!

#Ooopsie, I accidently typed command_prefix() instead of command_prefix =
#let's fix it real quick.
#Perfect 2!

#Now, in order to make the command as a whole accept command_name (or also called command_context), we will use a parameter that commands.Bot() uses
#in order to make it possible. It's called: case_insensitive=
#in our case, we want our command_name to be case_insensitive, so let's turn case_insensitive to True

#Peeeerfect!

############################################################################
#3. Now we will be adding a bot launch notification.

#Oh, let's just outline what we will be doing first.
#OK let's add a bot notif message

#this will allow us to know if the bot is running yet or not
#ooppppsie another mistake
#it's  on_ready():        and not just on_ready()
#let's fix it real quick


############################################################################Done

#4. Now, let's code the command

##Alright, xxx is basically the "command_name"
#we will be using something like crazy

##so, this means that our command will be as follow: !kranthos crazy

##have you noticed again? I just made another mistake

##it's crazy(ctx):           and not just crazy(ctx)
#let's fix it real quick.
#yum done.

############################################################################Done

#5. OK now, let's run our bot

#note here: token got to be private, it's like the password that allows you to access to your bot
#the token should be private
#you can get your bot taken at: https://discordapp.com/developers/applications/
#then choose your bot
#then go to bot> Bot > copy token. Et voilà.

#in case you don't have a bot in: https://discordapp.com/developers/applications/ you can simply create one by clicking on create a bot.

#I will put this link in the description so that you can find it real quick.

#Alrigt, we are done. Let's test this new case insensitive command.

#don't forget to copy paste your token in "token" it should give you a final result as follow:

#bot.run("gdfgdf4d3fg4df53g4-dfgdfg64f6-Yz")

#like this. i will put mine and test the bot.

#there is one last issue that we found when testing our bot which is

#the command is as follow: "prefixcommand" and not "prefix command"

#to fix this issue, simply add a space in your command_list #here

#now, let's restart the bot and re-test it

#it works.

#have a nice day. uwu
#and thanks for watching, hope that this tutorial will benefit you


import discord
from discord.ext import commands

##commands_list
command_list = ["!KRANTHOS ", "!kranthos ", "!Kranthos "] 

##defining the bot command prefix

bot = commands.Bot(command_prefix=commands.when_mentioned_or(*command_list), case_insensitive=True)

##Bot launch notif

@bot.event

async def on_ready():
    print('Kranthos Bot running!')

##command

@bot.command()

async def crazy(ctx):

    await ctx.send("Whoooaaa")

##running the bot

bot.run("e.i sddsf7jgsf6d5g-dhdg2hf4g4hf5gh-Yw#") #REPLACE THE TOKEN


#####################################################Done

