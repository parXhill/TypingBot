## This will be used to create a typing bot.

import pyautogui
import time
import random
import csv


def get_mode():

    mode = "mode error"

    if random.randint(1, 100) > 85:
        mode = get_break_value()
    else: 
        mode = get_typing_speed()
    
    return mode

def get_break_value():
    break_check_value = random.randint(1, 100) 

    break_time = "error"

    if break_check_value <= 50:
        break_time = ["short_break", alter_typing_speed(.26, .30)]

    elif break_check_value > 50 and break_check_value <= 85:
        break_time = ["medium_break", alter_typing_speed(.31, .38)]

    else:
        break_time = ["long_break", alter_typing_speed(.32, .40)]
        
    return break_time

def get_typing_speed():

    typing_check_value = random.randint(1, 100)

    speed = "speed error"

    if typing_check_value <= 50:
        speed = ["average_speed", alter_typing_speed(.12, .18)]

    elif typing_check_value > 50 and typing_check_value <= 80:
        speed = ["fast_speed", alter_typing_speed(.09, .14)]

    else:
        speed = ["slow_speed", alter_typing_speed(.20, .26)]

    return speed

def line_formula(line, repetitions, number_of_segments):
    
    lines_to_complete = repetitions

    segment_length = repetitions / number_of_segments
    print(segment_length)

    for i in range(number_of_segments):

        ##Decides the segment style and sets speed
        mode = get_mode()
        print(mode)
        interval = mode[1]

        ## Optional Pause 20% chance

        pause_chance = random.randint(1, 10) 
        if pause_chance > 7:
            pause_time = random.randint(1, 7) 
            time.sleep(pause_time)
            print("Break taken:", pause_time)

        for i in range(int(segment_length)):
            while lines_to_complete > 0:
                pyautogui.write(line, interval)
                lines_to_complete -= 1

def characters_per_minute(line, execution_time):

    line_length = len(line)

    characters_per_minute = 60 / execution_time * (line_length * repetitions)

    return characters_per_minute, line_length

def alter_typing_speed(min, max):
    random_interval= random.uniform(min, max)
    return random_interval

def line_time_test():
    for i in range(1):

        start_time = time.time()

        line_formula(line)

        end_time = time.time()

        execution_time = end_time - start_time

        data.append(["line-trial",f"{repetitions}lines", f"{round(execution_time, 2)}seconds", f"{characters_per_minute(line, execution_time)[1]}chars", f"{round(characters_per_minute(line, execution_time)[0])}cpm"])

def task_time_test(line, repetitions, number_of_segments):

    start_time = time.time()

    ## Set number of trials
    for i in range(1):

        ## Execute code
        line_formula(line, repetitions, number_of_segments)

    end_time = time.time()

    execution_time = end_time - start_time

    data.append(["task-trial", f"{repetitions*(i+1)}lines", f"{round(execution_time, 2)}seconds", f"{characters_per_minute(line, execution_time)[1]}chars", f"{round(characters_per_minute(line, execution_time)[0])}cpm"])

def add_data_to_csv():

    filename = 'linestests.csv'

    with open(filename, 'a', newline='') as csvfile:
    
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerows(data)

############################### FUNCTIONS ABOVE ##############################


data = []

line = "i must remember to do my homework."

repetitions = 14

number_of_segments = 7


############# PARAMETERS FOR TASK ABOVE ##############################
############# PROGRAM BELOW ##########################################

## 1. Pause while screen is selected

time.sleep(3)

## 2. Call line writing function

task_time_test(line, repetitions, number_of_segments)

add_data_to_csv()

############# LINE PRACTICES BELOW ##########################################
"""i must rememberi must remember i must rememberi must rememberi must rememberi must rememberi must rememberi must remember"""



##raise Exception('Stop Here')