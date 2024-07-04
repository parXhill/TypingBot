import random

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
        break_time = "short_break"

    elif break_check_value > 50 and break_check_value <= 85:
        break_time = "medium_break"

    else:
        break_time = "long_break"
        
    return break_time

def get_typing_speed():

    typing_check_value = random.randint(1, 100)

    speed = "speed error"

    if typing_check_value <= 50:
        speed = 'average_speed'

    elif typing_check_value > 50 and typing_check_value <= 80:
        speed = 'fast_speed'

    else:
        speed = 'slow_speed'

    return speed


mode_distribution = []
for i in range(40000):
    mode_distribution.append(get_mode())

print(mode_distribution.count("average_speed"))
print(mode_distribution.count("fast_speed"))
print(mode_distribution.count("slow_speed"))
print(mode_distribution.count("short_break"))
print(mode_distribution.count("medium_break"))
print(mode_distribution.count("long_break"))



