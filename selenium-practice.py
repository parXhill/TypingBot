from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path = '/Users/alexanderparkhill/chromedriver'

# Create a Service object
service = Service(driver_path)

# Initialize the ChromeDriver
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get('https://www.google.com')

# Find the search box element
search_box = driver.find_element(By.NAME, 'q')

# Enter text into the search box
search_box.send_keys('Where is the best kind of soup in Melbourne?')
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.quit()