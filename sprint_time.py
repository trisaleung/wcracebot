import discord
from discord.ext import commands

import time
import datetime
import schedule
import config
import threading

async def timer(time_given):
    global toc = time.time()

    while True:
        global tic = time.time()
        if tic - toc >= (time_given * 60):
            return

@config.bot.event
async def sprint_end(ctx, time_end):
    timer(time_end)

    schedule.clear("timer")
    await ctx.send("Sprint finished!")

@config.bot.event
async def sprint_start(ctx, time_start):
    timer(time_start)

    await ctx.send("Sprint starting!")
    schedule.clear("timer")

@config.bot.event
async def sprint_wait(ctx, start_time):
    schedule.every(start_time).minutes.do(sprint_start).tag("timer")

@config.bot.event
async def sprint_run(ctx, end_time):
    schedule.every(end_time).minutes.do(sprint_end).tag("timer")

def only_one_sprint():
    #TODO: ensures there is only one sprint happening
    #PRIORITY
    return

def sprint_ranks():
    #TODO: returns sprint ranks
    return

def level_up():
    #TODO: interact with database to level people up
    return