import discord
from discord.ext import commands

import config
import sprint_time
import schedule

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

        await sprint_time.sprint_wait(ctx, int(arg3))
        await sprint_time.sprint_start(ctx, int(arg3))

        await sprint_time.sprint_run(ctx, int(arg1))
        await sprint_time.sprint_end(ctx, int(arg1))

config.bot.run("XXXXX")
