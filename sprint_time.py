import discord
from discord.ext import commands
import time
import datetime
import schedule
import config

@config.bot.event
async def sprint_end(ctx, time_end):
    toc = time.time()

    while True:
        tic = time.time()
        if tic-toc >= (time_end * 60):
            break

    schedule.clear("timer")
    await ctx.send("Sprint finished!")

@config.bot.event
async def sprint_start(ctx, time_start):
    toc = time.time()

    while True:
        tic = time.time()
        if tic-toc >= (time_start * 60):
            break

    await ctx.send("Sprint starting! Get writing, @here!")
    schedule.clear("timer")

@config.bot.event
async def sprint_wait(ctx, start_time):
    schedule.every(start_time).minutes.do(sprint_start).tag("timer")

@config.bot.event
async def sprint_run(ctx, end_time):
    schedule.every(end_time).minutes.do(sprint_end).tag("timer")