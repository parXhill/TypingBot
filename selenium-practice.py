from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import random
from typingbot import get_typing_speed, pause_chance, add_mistake_chance

driver_path = '/Users/alexanderparkhill/chromedriver'

# Create a Service object
service = Service(driver_path)

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-features=EnableEphemeralFlashPermission')


# Initialize the ChromeDriver with the options
driver = webdriver.Chrome(service=service, options=chrome_options)

#---------------------------Functions---------------------------------#

def interruption_loop():
    print("Interruption Loop Started")
    time.sleep(2)
    while check_for_interruption_screen():
        print("Continuing Interruption Loop")
        time.sleep(1)
    print("Exiting Interruption Loop")
    time.sleep(2)

def mistake_loop():
    print("Mistake Loop Started")
    time.sleep(2)
    while check_for_mistake():
        print("Continuing Mistake Loop")
        time.sleep(1)
    print("Exiting Mistake Loop")
    time.sleep(2)
      
def check_for_interruption_screen():
    try: 
        interruption_overlay = driver.find_element(By.ID, 'interruptionOverlay')
        if interruption_overlay.is_displayed():
            return True
    except:
        return False

def check_for_mistake():
    try: 
        mistake_overlay = driver.find_element(By.ID, 'mistakeOverlay')
        if mistake_overlay.is_displayed():
            return True
    except:
        return False

def issues_check():

    mistake_check = check_for_mistake()
    interruption_check = check_for_interruption_screen()

    if mistake_check == True:
        print('Mistake Screen Detected: Entering mistake loop')
        mistake_loop()
        return "mistake"

    if interruption_check == True:
        print('Interruption screen detected: Entering interruption loop')
        interruption_loop()
        return "interruption"

def split_into_chunks(line, chunk_size):
    return [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]

def type_line(line, interval):
    
    print('Entered type_line')
    
    # Break line up into chunks or individual characters

    list_of_chunks = split_into_chunks(line, 1)

    print(list_of_chunks)

    for chunk in list_of_chunks:

        issue = issues_check()

        if issue == "mistake":
            print("Mistake loop finished: Returning to main function")
            return False
        
        elif issue == "interruption":
            print("Interruption loop finished: Continuing")
            pyautogui.write(chunk, interval)
            print(chunk)

        else: 
            pyautogui.write(chunk, interval)
            print(chunk)

    return True  
    
def selenium_write_lines(line, lines_set):

    time.sleep(2)

    total_lines = lines_set
    print("Original total_lines:", total_lines)

    while lines_set > 0:
        
        print("Remaining lines:", lines_set)      

        ##Sets mode (typing interval speed)

        typing_speed = get_typing_speed()
        print(typing_speed)
        interval = typing_speed[1]

        ## Chance to pause between lines
        took_pause = pause_chance()
        if took_pause:
            print("Pause taken")

        ## Chance for intentional mistakes, adds lines
        made_mistake = add_mistake_chance(line)

        if made_mistake:
            print("Intentional Mistake Made")
            lines_set += 1
            total_lines +=1

        else: 
            if type_line(line, interval):
                lines_set -= 1
            
    print(total_lines)
    return total_lines


#---------------------------Opening page---------------------------------#
# Open the webpage
driver.get('https://www.typeforme.net/task/43c2042309fb4eb8bb687a5744c198f1')

# Wait for the 'accept' button
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'v-btn--elevated')))

# Define the button
button = driver.find_element(By.CLASS_NAME, 'v-btn--elevated')

# Click the button
button.click() 



# Wait until the task becomes visible
wait = WebDriverWait(driver, 10)
task_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/task/18ebf592ecc1432b848106a7879cf8c7"]')))

# Click the element
task_link.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'v-btn') and contains(., 'Start the task')]")))

# Button to start task on intro screen
new_button= driver.find_element(By.XPATH, "//button[contains(@class, 'v-btn') and contains(., 'Start the task')]")
new_button.click()

# Pause before starting to type
print("Arrived on page, starting typing cycle in 3 seconds")
time.sleep(2)


#---------------------------Typing begins---------------------------------#

## Trigger initial mistake to prevent capital letter issue


## Complete the task

selenium_write_lines("it is extremely important to write this line only using lower-case letters.", 70)


# Wait to observe results before browser closes

time.sleep(35)


#----- unneeded? --------#
