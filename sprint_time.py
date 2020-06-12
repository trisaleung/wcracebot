import discord
from discord.ext import commands
import time
import schedule
import datetime

import config

def sprint_end(time_remaining):
    print("DEBUGGING: SPRINT END")

    sprint_timer(time_remaining, False)

    #await message.channel.send("Sprint end!")
    return schedule.CancelJob

def sprint_start(time_remaining):
    print("DEBUGGING: SPRINT START")

    sprint_timer(time_remaining, True)

    #await message.channel.send("Sprint start!")
    return schedule.CancelJob

#gives time remaining
def sprint_timer(time_remaining, sprint_run):
    print("DEBUG: TO DELETE")

#sets the starting and end time in scheduler
def set_times(start_time, end_time):
    length_of_wrap_around=0
    start_minutes='0'
    start_seconds='0'
    end_minutes='0'
    end_seconds='0'
    length_of_sprint=0
    time_remaining = length_of_sprint

    print("DEBUGGING: SETTING TIME")

    if int(start_time) < 0:
        return "Sprint cannot run in negative time."

    #starting time
    now = datetime.datetime.now()

    print(now)

    start_minutes = str(int(now.minute) + int(start_time))
    start_seconds = str(now.second)

    print("DEBUGGING: " + start_minutes)
    print(schedule.every(int(start_time)).minutes.do(sprint_start(time_remaining)))

    #ending time
    temp = int(start_minutes) + int(end_time)

    while temp >= 60:
        temp -= 60
        length_of_wrap_around += 1
        end_minutes = str(temp)

    end_seconds = start_seconds

    print("DEBUGGING: " + end_minutes)
    print(schedule.every(int(end_time)).minutes.do(sprint_end(time_remaining)))

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