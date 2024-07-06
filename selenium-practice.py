from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui


def typer_call():
    time.sleep(2)
    pyautogui.write("Slave Degradation", 0.04)
    return " "

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

# Open a webpage
driver.get('https://www.typeforme.net/task/43c2042309fb4eb8bb687a5744c198f1')

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'v-btn--elevated')))

# Find the search box element
#search_box = driver.find_element(By.ID, 'input-119')
button = driver.find_element(By.CLASS_NAME, 'v-btn--elevated')

# Click the button
button.click()
time.sleep(3)

# Enter text into the search box

#search_box = driver.find_element(By.CLASS_NAME, "v-field__input")

#search_box.click()
#time.sleep(1)
#search_box.send_keys(typer_call())
#time.sleep(1)
#search_box.send_keys(Keys.RETURN)
#time.sleep(3)

wait = WebDriverWait(driver, 10)
element2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/task/43c2042309fb4eb8bb687a5744c198f1"]')))

# Click the element
element2.click()


# Find and click the task button

#wait = WebDriverWait(driver, 10)
#element3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c833b5acc9aa45eaa79d0d18692cfb0a"]/div[1]/div/div[4]/div/div[2]/button')))

#element3.click()


#Interruption checks


def interruption_loop():
    print("Entering Interruption Loop")
    while check_for_interruption_screen():
        print("Interruption Loop")
        time.sleep(1)
    print("Exiting Interruption Loop")

def mistake_loop():
    print("Entering Mistake Loop")
    while check_for_mistake():
        print("Mistake Loop")
        time.sleep(1)
    print("Exiting Mistake Loop")
    time.sleep(1)
      

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

########## Execution here ###########

print("Arrived on page, starting typing cycle in 3 seconds")
time.sleep(4)

## Initial mistake trigger

pyautogui.write("z", 0.1)

for i in range(25):
    
    mistake_check = check_for_mistake()
    interruption_check = check_for_interruption_screen()

    if mistake_check == True:
        print('Mistake Screen Detected')
        mistake_loop()

    if interruption_check == True:
        print('Interruption screen detected')
        interruption_loop()
        #Trigger a mistake to return to the start of the line.
        pyautogui.press('enter')
   
    else:
        if random.randint(1,100) < 90:
            print("Writing Standard Line")
            pyautogui.write("I must do my Homework on time.", 0.05)
        else:
            print("Writing Mistake Line")
            pyautogui.write("I mustr", 0.05)



# Wait for a few seconds to see the results
time.sleep(3)


