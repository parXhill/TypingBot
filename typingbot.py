## This will be used to create a typing bot.

import pyautogui
import time
import random
import csv


def bootup(initial_delay, secondary_delay):
    
    time.sleep(initial_delay)

    pyautogui.write(f"Will start writing lines in {secondary_delay} seconds", 0.01)

    time.sleep(secondary_delay)

def pause_chance():

    pause_chance = random.randint(1, 10) 
    if pause_chance >= 10:
        pause_time = random.randint(1, 5) 
        time.sleep(pause_time)
        return True

def get_mode():

    mode = "mode error"

## Setting the chance of a break:
    if random.randint(1, 100) > 85:
        mode = get_typing_speed() ##### ALTERED-SWITCHED-WITH-BREAK ########
        print(mode)
    else: 
        mode = get_typing_speed()
        print(mode)
    
    return mode

def get_break_value():

    ## Decides the speed of the typing break period
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

    ## Decides the typing speed per segment
    typing_check_value = random.randint(1, 100)

    speed = "speed error"

    if typing_check_value <= 50:
        speed = ["average_speed", alter_typing_speed(.12, .18)]

    elif typing_check_value > 50 and typing_check_value <= 80:
        speed = ["fast_speed", alter_typing_speed(.09, .14)]

    else:
        speed = ["slow_speed", alter_typing_speed(.20, .26)]

    return speed

def original_write_lines(line, lines_set):

    total_lines = lines_set
    print("Original total_lines:", total_lines)

    while lines_set > 0:
        
        print("Remaining lines:", lines_set)      

        ##Sets mode (typing interval speed)
        mode = get_mode()
        interval = mode[1]

        ## Chance to pause between lines
        took_pause = pause_chance()
        if took_pause:
            print("Pause taken")

        ## Chance to pause between lines
        made_mistake = add_mistake_chance(line)

        if made_mistake:
            print("Made mistake")
            lines_set += 1
            total_lines +=1

        else: 
            pyautogui.write(line, interval)
            lines_set -= 1
            print("Line completed")
    
    return total_lines

def characters_per_minute(line, execution_time, total_lines):

    line_length = len(line)

    characters_per_minute = 60 / execution_time * (line_length * total_lines)

    return characters_per_minute, line_length

def alter_typing_speed(min, max):
    random_interval= random.uniform(min, max)
    return random_interval

def task_time_test(line, lines_set):

    start_time = time.time()

    total_lines = write_lines(line, lines_set)

    end_time = time.time()

    execution_time = end_time - start_time

    data.append([f"{total_lines}total lines", f"{round(execution_time, 2)}seconds", f"{characters_per_minute(line, execution_time)[1]}chars", f"{round(characters_per_minute(line, execution_time)[0])}cpm", f"Mistakes:{total_lines - lines_set}"])

def add_data_to_csv():

    filename = 'linestests.csv'

    with open(filename, 'a', newline='') as csvfile:
    
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerows(data)

def add_mistake_chance(line):
    
    # Sets mistake chance
    mistake_chance = random.randint(1, 100)

    if mistake_chance > 100: #ALTERED FOR NO MISTAKES

        # Chooses mistake character
        mistake_indices = [0, 1, -1, -2]
        mistake_index_selector = random.randint(0,3)
        pyautogui.write(line[mistake_indices[mistake_index_selector]], 0.1)
        time.sleep(4)
        return True
    else:
        return False

############################### FUNCTIONS ABOVE ##############################


#data = []

#line = "It is better for me to type this than to be getting up to anything more mischievous."

#lines_set= 30

############# EXECUTE PROGRAM BELOW ##########################################

## 1. Call bootup to initialize, preventing first letter being wrongly uncapitalized

##bootup(initial_delay = 1, secondary_delay = 2)

## 2. Call line writing function

##task_time_test(line, lines_set)

## 3. Add test data to CSV

##add_data_to_csv()

############# LINE PRACTICES BELOW ##########################################and yo
""""""
