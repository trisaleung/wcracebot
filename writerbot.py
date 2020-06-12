import discord
from discord.ext import commands

import config
import sprint_time

import schedule
import asyncio

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/Desktop/writerbot')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@config.bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(config.bot))

@config.bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@config.bot.command()
async def sprint(ctx, arg1, arg2, arg3):
    if arg2 != "in":
        await ctx.send("Invalid command.")
    elif int(arg1) < 0 and int(arg3) < 0:
        await ctx.send("Invalid command.")
    else:
        await ctx.send("A sprint has been scheduled for {} minutes in {} minutes. Join sprint with ``-join <wc>``".format(arg1, arg3))
        
        await sprint_time.sprint_start(ctx, int(arg3))
        #schedule.every(int(arg3)).minutes.do(sprint_time.sprint_start, ctx)
        
        await sprint_time.sprint_end(ctx, int(arg1))

@config.bot.command()
async def join(ctx, arg1):
    return

@config.bot.command()
async def time(ctx):
    await ctx.send("Time remaining: ")

@config.bot.command()
async def quit(ctx):
    await ctx.send("Quitting sprint.")

config.bot.run(DISCORD_TOKEN)