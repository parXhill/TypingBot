import pyautogui
import time
import random
import csv


# ---------------- Functions ----------------#
# Inserts mistakes at random intervals
def add_mistake_chance(line):

    # Sets mistake chance
    mistake_chance = random.randint(1, 100)

    if mistake_chance > 101:

        # Chooses mistake character
        mistake_indices = [0, 1, -1, -2]
        mistake_index_selector = random.randint(0, 3)
        pyautogui.write(line[mistake_indices[mistake_index_selector]], 0.1)
        print(line[mistake_indices[mistake_index_selector]])
        time.sleep(4)
        return True
    else:
        return False


# Takes breaks at random intervals
def break_chance():

    break_chance = random.randint(1, 10)
    if break_chance >= 10:
        break_time = random.randint(1, 5)
        time.sleep(break_time)
        return True


# Sets random typing speeds for each line
def get_typing_speed():

    ## Setting the chance of a break:

    speed_check_value = random.randint(1, 100)

    if speed_check_value > 0 and speed_check_value <= 5:
        typing_speed = ["speed 1/6", alter_typing_speed(0.25, 0.30)]

    elif speed_check_value > 5 and speed_check_value <= 10:
        typing_speed = ["speed 2/6", alter_typing_speed(0.20, 0.25)]

    elif speed_check_value > 10 and speed_check_value <= 20:
        typing_speed = ["speed 3/6", alter_typing_speed(0.11, 0.20)]

    elif speed_check_value > 20 and speed_check_value <= 40:
        typing_speed = ["speed 4/6", alter_typing_speed(0.06, 0.10)]

    elif speed_check_value > 40 and speed_check_value <= 80:
        typing_speed = ["speed 5/6", alter_typing_speed(0.03, 0.06)]

    else:
        typing_speed = ["speed 6/6", alter_typing_speed(0.01, 0.03)]

    return typing_speed


# ---------------- IGNORE: FOR TESTING PURPOSES ----------------#
def non_selenium_write_lines(line, lines_set):

    total_lines = lines_set
    print("Original total_lines:", total_lines)

    while lines_set > 0:

        print("Remaining lines:", lines_set)

        ##Sets mode (typing interval speed)
        mode = get_typing_speed()
        interval = mode[1]

        ## Chance to pause between lines
        took_break = break_chance()
        if took_break:
            print("Break taken")

        ## Chance to pause between lines
        # made_mistake = add_mistake_chance(line)

        # if made_mistake:
        # print("Made mistake")
        # lines_set += 1
        # total_lines +=1

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
    random_interval = random.uniform(min, max)
    return random_interval


def task_time_test(line, lines_set):

    start_time = time.time()

    total_lines = non_selenium_write_lines(line, lines_set)

    end_time = time.time()

    execution_time = end_time - start_time

    data.append(
        [
            f"{total_lines}total lines",
            f"{round(execution_time, 2)}seconds",
            f"{characters_per_minute(line, execution_time)[1]}chars",
            f"{round(characters_per_minute(line, execution_time)[0])}cpm",
            f"Mistakes:{total_lines - lines_set}",
        ]
    )


def add_data_to_csv():

    filename = "linestests.csv"

    with open(filename, "a", newline="") as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerows(data)


def bootup(initial_delay, secondary_delay):

    time.sleep(initial_delay)

    pyautogui.write(f"Will start writing lines in {secondary_delay} seconds", 0.01)

    time.sleep(secondary_delay)


data = []

pyautogui.write("i", 2)

time.sleep(3)


non_selenium_write_lines(
    "I'm a slave. Pain is my pleasure. I'm a slave. Pain is my life",
    11,
)

"i am a good boyi who ilovesi writing lines. Writing linieiiiiJsem stara, zasrana otrocka buzna.Posrana plina je moje uniforma. Teply chcanky jsou moje voda. Vysrany hovna jsou mj chleb.Jsem stara, zas makes me a good boy for MasterI am a good boy who loves writing lines. writing lines makes me a good boy for MasterI am a good boy who loves wri am a good boy who loves writing s. Writing lines m  good boy for MasterI am  loves writing lines. Writing liiI am a good boy who loves writing lines. writing lines makes me a good boy for masterI nes makes me a good boyiiiI am a good boy who loves writing lines. Wrii for Masteri am ia good boy whi am a good boy who loves writ"
