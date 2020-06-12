import discord
from discord.ext import commands
import time
import datetime

import schedule

import config

@config.bot.event
async def sprint_end(ctx, end_time):
    print("DEBUGGING: SPRINT END")
    # now = datetime.datetime.now()
    
    # end_minutes = now.minute + end_time
    # end_seconds = now.second

    # if end_seconds < 10:
    #     await ctx.send("Sprint will end at **:" + str(end_minutes) + ":0" + str(end_seconds) + "**!")
    # elif end_minutes < 10:
    #     "Sprint will end at **:0" + str(end_minutes) + ":" + str(end_seconds) + "**!"
    # else:
    #     await ctx.send("Sprint will end at **:" + str(end_minutes) + ":" + str(end_seconds) + "**!")


    # while end_time > 5:
    #     time.sleep(1 * 60)
    #     end_time -= 1
    
    # if end_time == 5:
    #     await ctx.send("Sprint will begin in **" + str(end_time) + "** minute(s).")

    # while end_time  > 3:
    #     time.sleep(1 * 60)
    #     end_time -= 1
    
    # if end_time == 3:
    #     await ctx.send("Sprint will begin in **" + str(end_time) + "** minute(s).")

    # while end_time > 1:
    #     time.sleep(1 * 60)
    #     end_time -= 1
    
    # if end_time == 1:
    #     await ctx.send("Sprint will begin in **" + str(end_time) + "** minute.")

    # time.sleep(end_time * 60)

    # await ctx.send("Sprint has ended! Please enter your wcs!")

@config.bot.event
async def start_sprint(ctx):
    ctx.send("DEBUGGING: sprint starting!")

    return schedule.CancelJob


@config.bot.event
async def sprint_start(ctx, start_time):
    print("DEBUGGING: SPRINT START")

    print(schedule.every(start_time).minutes.do(start_sprint))

    # while start_time > 5:
    #     time.sleep(1 * 60)
    #     start_time -= 1
    
    # if start_time == 5:
    #     await ctx.send("Sprint will begin in **" + str(start_time) + "** minute(s).")

    # while start_time > 3:
    #     time.sleep(1 * 60)
    #     start_time -= 1
    
    # if start_time == 3:
    #     await ctx.send("Sprint will begin in **" + str(start_time) + "** minute(s).")

    # while start_time > 1:
    #     time.sleep(1 * 60)
    #     start_time -= 1
    
    # if start_time == 1:
    #     await ctx.send("Sprint will begin in **" + str(start_time) + "** minute.")

    # time.sleep(start_time * 60)
    # await ctx.send("Sprint will now begin! Start writing!")

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