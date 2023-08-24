import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rolandos.net/flashcards/editor.html?language=1")

with open("output.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    i = 0
    rows = []
    for row in csv_reader:
            rows.append(row)
    
    for r in range(600,650):
        first_input = driver.find_element(by=By.ID, value="mainQuestionInput")
        first_input.send_keys(rows[r][0])

        first_input.send_keys(Keys.TAB)

        second_input = driver.find_element(by=By.ID, value="mainSolutionInput")
        second_input.send_keys(rows[r][1])

        second_input.send_keys(Keys.ENTER)

        i += 1
        print(r+1)
        if i == 50:
            break

time.sleep(2000000)