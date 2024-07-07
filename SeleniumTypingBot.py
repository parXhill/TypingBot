from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from PyAutoGuiFunctions import get_typing_speed, break_chance, add_mistake_chance


#---------------------------Functions---------------------------------#

# Initializes the Selenium driver
def initialize_selenium_driver(path):
    
    driver_path = path

    # Create a Service object
    service = Service(driver_path)

    # Set options
    chrome_options = webdriver.ChromeOptions()

    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-features=EnableEphemeralFlashPermission')


    # Initialize driver with options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

# Opens the browser and navigates to the task page
def open_task(task_URL):

    # Opens the webpage
    driver.get('https://www.typeforme.net')

    # Wait for the 'accept terms' button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'v-btn--elevated')))

    # Create 'accept terms' button element
    accept_terms_button = driver.find_element(By.CLASS_NAME, 'v-btn--elevated')

    # Click 'accept terms' button
    accept_terms_button.click() 


    # Wait until the specific task option becomes visible
    wait = WebDriverWait(driver, 10)

    # Go to specific task page

    driver.get(f'{task_URL}')

    # Deal with optional introduction screen
    try: 
        #Wait for introduction screen 'accept' button to appear 
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'v-btn') and contains(., 'Start the task')]")))
        
        # Button to start task on intro screen
        start_task_button= driver.find_element(By.XPATH, "//button[contains(@class, 'v-btn') and contains(., 'Start the task')]")
        start_task_button.click()
        
    except: 
        pass

    # Confirm arrival on page
    time.sleep(1)
    print("Arrived on task page.")

# Finds the initial line string to write 
def get_initial_line():
    initial_line_element = driver.find_element(By.ID, 'lineToTypeInitial')
    initial_line = initial_line_element.text
    print("Initial line to type:", initial_line)
    return initial_line

# Starts the task, triggering the DOM to reveal the task details
def initialize_task():

    line = get_initial_line()

    #Writes the first character to trigger DOM changes that reveal total lines 
    pyautogui.write(line, 0.1)

    time.sleep(2)

    return line

# Organizes the writing of the sentences
def write_lines():

    #Get the line from the DOM and writes first character 
    line = initialize_task()

    #Reads number of lines needed from the DOM
    lines_remaining = get_remaining_lines()

    while lines_remaining > 0:
        
        print("Remaining lines:", lines_remaining)      

        #Sets typing speed
        typing_speed = get_typing_speed()
        print(typing_speed)

        #Chance to take a break between lines
        took_break = break_chance()

        if took_break:
            print("Pause taken")

        #Chance for intentional mistake
        made_intentional_mistake = add_mistake_chance(line)

        if made_intentional_mistake:
            print("Intentional Mistake Made")

        else: 
            type_line(typing_speed)
        
        #Re-calculated number of lines needed
        lines_remaining = get_remaining_lines()

# Types each line 
def type_line(typing_speed):

    #Set the interval between character strokes
    interval = typing_speed[1]

    #Find the line to type in the DOM
    line_to_type_element = driver.find_element(By.ID, 'lineToTypeCurrent')
    line_to_type = line_to_type_element.text

    #Loop through the characters in the line
    for character in line_to_type:

        #Check for mistake or interruption screens
        issue = issues_check()

        if issue == "mistake":
            print("Mistake loop finished: Returning to main function")
            return False
        
        elif issue == "interruption":
            print("Interruption loop finished: Continuing")
            pyautogui.write(character, interval)
            print(character)

        else: 
            #Write the character
            pyautogui.write(character, interval)
            print(character)

    return True  

# Keeps track of the amount of lines to write
def get_remaining_lines():

    lines_remaining_element = driver.find_element(By.XPATH, '//tr/td[@class="text-right"]')
    lines_remaining = lines_remaining_element.text
    print("Lines Remaining: ", lines_remaining)
    return int(lines_remaining)

# Identifies issues such as mistakes, or screen interruptions
def issues_check():

    #-----------FUNCTIONS-----------#

    # Checks for an interruption screen
    def check_for_interruption_screen():
        try: 
            interruption_overlay = driver.find_element(By.ID, 'interruptionOverlay')
            if interruption_overlay.is_displayed():
                return True
        except:
            return False

    # Checks for mistakes
    def check_for_mistake():
        try: 
            mistake_overlay = driver.find_element(By.ID, 'mistakeOverlay')
            if mistake_overlay.is_displayed():
                return True
        except:
            return False

    # Loops until interruption screen is no longer displayed
    def interruption_loop():
        print("Interruption Loop Started")
        time.sleep(2)
        while check_for_interruption_screen():
            print("Continuing Interruption Loop")
            time.sleep(1)
        print("Exiting Interruption Loop")
        time.sleep(2)

    # Loops until mistake screen is no longer displayed
    def mistake_loop():
        print("Mistake Loop Started")
        time.sleep(2)
        while check_for_mistake():
            print("Continuing Mistake Loop")
            time.sleep(1)
        print("Exiting Mistake Loop")
        time.sleep(2)


    #-----------ISSUES CHECK-----------#
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


#--------------------------- Program ---------------------------------#

# Initialize driver on local path

pyautogui.write('a', 0.1)
""" a"""

driver = initialize_selenium_driver(path= '/Users/zadavalivoprosov/chromedriver')

# Open the task with the URL
open_task(task_URL="https://www.typeforme.net/task/580a1d44cc06412487086a70d6654acfa")

# Start typing
write_lines()

print("Finished typing lines")

