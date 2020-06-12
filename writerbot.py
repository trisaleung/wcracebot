import discord
from discord.ext import commands

import config
import sprint_time

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/Desktop/writerbot')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@config.bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(config.bot))

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('-hello'):
#         await message.channel.send('Hello!')

@config.bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@config.bot.command()
async def sprint(ctx, arg1, arg2, arg3):
    if arg2 != "in":
        pass
    else:
        await ctx.send("Sprinting for {} minutes in {} minutes".format(arg1, arg3))
        
        sprint_time.set_times(arg3, arg1)

        # if int(arg3) == 0:
        #     await ctx.send("Starting sprint now!")
        #     sprint_time.sprint_timer(int(arg1))
        #     await ctx.send("Sprint is over!")
            
        # elif int(arg3) > 0:
        #     sprint_time.timer_to_sprint(int(arg3))
        #     await ctx.send("Starting sprint now!")

        #     sprint_time.sprint_timer(int(arg1))
        #     await ctx.send("Sprint is over!")
        # else:
        #     await ctx.send("Negative sprint time not allowed.")

@config.bot.command()
async def time(ctx):
    await ctx.send("Time remaining:")

@config.bot.command()
async def quit(ctx):
    await ctx.send("Quitting sprint.")

config.bot.run(DISCORD_TOKEN)