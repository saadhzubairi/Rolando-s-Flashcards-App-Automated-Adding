from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://rolandos.net/flashcards/editor.html?language=1') 

# Find the first input field and enter the first text
first_input = driver.find_element(by=By.ID,value='mainQuestionInput') 
first_input.send_keys('First text')

# Press the Tab key
first_input.send_keys(Keys.TAB)

# Find the second input field and enter the second text
second_input = driver.find_element(by=By.ID,value='mainSolutionInput')  
second_input.send_keys('Second text')

# Press the Enter key
second_input.send_keys(Keys.ENTER)

# Wait for a moment before closing the browser
time.sleep(2)