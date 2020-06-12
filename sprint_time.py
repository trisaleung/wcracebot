import discord
from discord.ext import commands
import time
import schedule
import datetime

import config

@config.bot.event
async def sprint_end(ctx, end_time):
    print("DEBUGGING: SPRINT END")

    await ctx.send("Sprint has ended! Please enter your wcs!")

    return schedule.CancelJob

@config.bot.event
async def sprint_start(ctx, start_time):
    print("DEBUGGING: SPRINT START")


    await ctx.send("Sprint will now begin! Start writing!")

    return schedule.CancelJob

# #gives time remaining
# def sprint_timer(time_remaining, wrap_around, sprint_run):
#     time_left=0
#     now = datetime.datetime.now()
#     minutes_goal = now.minute

#     if wrap_around == 0:
#         time_left -= minutes_goal - time_remaining
#     else:
#         minutes_goal += (60 * wrap_around)
#         time_left -= minutes_goal - time_remaining

#     print(time_left + " remaining!")

#     return minutes_goal

# #sets the start time in the scheduler
# def set_start(start_time):
#     length_of_wrap_around_beginning=0
#     start_minutes='0'
#     start_seconds='0'

#     print("DEBUGGING: SETTING TIME")

#     if int(start_time) < 0:
#         return "Sprint cannot run in negative time."

#     #starting time
#     now = datetime.datetime.now()

#     start_minutes = str(int(now.minute) + int(start_time))
#     start_seconds = str(now.second)

#     temp = int(start_minutes)

#     while temp >= 60:
#         temp -= 60
#         length_of_wrap_around_beginning += 1
#         start_minutes = str(temp)

#     time_remaining = start_time
#     print("DEBUGGING: " + start_minutes)
#     schedule.every(int(start_time)).minutes.do(sprint_start, time_remaining, length_of_wrap_around_beginning)

# #sets the end time in the scheduler
# def set_end(end_time):
#     length_of_wrap_around_end=0
#     length_of_sprint=int(end_time)

#     #ending time
#     now = datetime.datetime.now()

#     temp = int(now.minute) + int(end_time)
#     end_minutes = temp

#     while temp >= 60:
#         temp -= 60
#         length_of_wrap_around_end += 1
#         end_minutes = str(temp)

#     end_seconds = now.second

#     time_remaining = length_of_sprint
#     print("DEBUGGING: " + end_minutes)
#     schedule.every(int(end_time)).minutes.do(sprint_end, time_remaining, length_of_wrap_around_end)

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


# def sprint_timer(length_of_sprint):
#     length_of_sprint *= 60

#     while length_of_sprint > 0:
#         length_of_sprint -= 1
#         time.sleep(1)
    
# def timer_to_sprint(time_to_start):
#     time_to_start *= 60

#     while time_to_start > 0:
#         time_to_start -= 1
#         time.sleep(1)