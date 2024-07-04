## This will be used to create a typing bot.

import pyautogui
import time
import random
import csv

def write_line(some_line):
    interval = alter_typing_speed()
    pyautogui.write(some_line, interval)

def line_formula(some_line):
    for i in range(repetitions):
        write_line(some_line)

def characters_per_minute(line, execution_time):

    line_length = len(line)

    characters_per_minute = 60 / execution_time * (line_length * repetitions)

    return characters_per_minute, line_length

def alter_typing_speed():
    random_interval= random.uniform(0.1, 0.25)
    return random_interval

def line_time_test():
    for i in range(1):

        start_time = time.time()

        line_formula(line)

        end_time = time.time()

        execution_time = end_time - start_time

        data.append(["line-trial",f"{repetitions}lines", f"{round(execution_time, 2)}seconds", f"{characters_per_minute(line, execution_time)[1]}chars", f"{round(characters_per_minute(line, execution_time)[0])}cpm"])

def task_time_test():

    start_time = time.time()
    for i in range(1):
        line_formula(line)

    end_time = time.time()

    execution_time = end_time - start_time

    data.append(["task-trial", f"{repetitions*(i+1)}lines", f"{round(execution_time, 2)}seconds", f"{characters_per_minute(line, execution_time)[1]}chars", f"{round(characters_per_minute(line, execution_time)[0])}cpm"])

############################### FUNCTIONS ABOVE ##############################

data = []

line = "i must remember to do my homework."

repetitions = 3

time.sleep(3)

task_time_test()

##raise Exception('Stop Here')
"""my emy evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster.vening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster. my evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster."""
## Time testing 






#Start program

##time.sleep(3)



##Insert line practices here:
"""mymymy eveni evening belongs to linemaster.my evening belongs to linemaster.my evening belo evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to linemaster.my evening belongs to LineMaster.my evening belongs to lineMaster.my evening belongs to LineMaster.my evening belongs to LineMaster.my evening belongs to LineMaster.my evening belongs to LineMaster.my evenmy evenmy evening belongs to Linemaster.my evening belongs to linemaster.ing belongs to LineMaster.ing belongmy evening belongs to LineMaster.My evening belongs to linemaster.my evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to linemaster.my evening belongs to LineMaster.My evening belongsmy evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to linemaster. to LineMaster.My evening belongs to LineMaster.s to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.my evening belongs to linemaster.my evening belongs to LineMaster.my evening belongs to lineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.My evening belongs to LineMaster.
"""



## Create a CSV for testing data.

filename = 'linestests.csv'

with open(filename, 'a', newline='') as csvfile:
 
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerows(data)

