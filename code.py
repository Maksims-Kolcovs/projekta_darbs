import selenium
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from tkinter import simpledialog, Tk

root = Tk()
root.withdraw()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
wait = WebDriverWait(driver, 30)

url = "https://www.youtube.com/watch?v=7ESeQBeikKs"

driver.get(url)
sleep(5)

driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button").click()
sleep(1)

try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='expand']")))
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")

sleep(1)

try:
    show_transcript = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primary-button']/ytd-button-renderer/yt-button-shape/button")))
    show_transcript.click()
except Exception as e:
    print(f"An error occured: {e}")

sleep(3)

try:
    element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='body']/ytd-transcript-segment-list-renderer")))
    actions = ActionChains(driver)
    actions.move_to_element(element2).perform()
    transcript = element2.text
    print(transcript)
except Exception as e:
    print(f"An error occurred: {e}")

lines = transcript.strip().split('\n')
transcript_pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]

with open('C:/Users/maksi/transcript.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Text"])  
    writer.writerows(transcript_pairs)