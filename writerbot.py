import discord
from discord.ext import commands

import config
import sprint_time

import schedule
import threading

@config.bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(config.bot))

@config.bot.command()
async def sprint(ctx, arg1, arg2, arg3):
    if arg2 != "in":
        await ctx.send("Invalid command.")
    elif int(arg1) < 0 and int(arg3) < 0:
        await ctx.send("Invalid command.")
    else:
        await ctx.send(
            "A sprint has been scheduled for {} minutes in {} minutes. Join sprint with ``-join <wc>``".format(
                arg1, arg3))
        
        def check(m):
            return m.content == 'hello'

        msg = await config.bot.wait_for("-join", check=check)

        await sprint_time.sprint_wait(ctx, int(arg3))
        await sprint_time.sprint_start(ctx, int(arg3))

        await sprint_time.sprint_run(ctx, int(arg1))
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

@config.bot.command()
async def prompt(ctx):
    await ctx.send("prompt here.")

config.bot.run("XXXXXX")
