import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox

root = tk.Tk()
root.withdraw()

# Logs, kurā var ielikt video url 

video_url = simpledialog.askstring("Ievade", "Lūdzu ievadiet video URL linku:", parent=root)


# Selenium inicializēšana
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
driver.maximize_window()
wait = WebDriverWait(driver, 15)


driver.get(video_url)
sleep(5)


# Uzspiež, ka apstiprina cookies 

driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button").click()
sleep(3)



# Uzspiež "...more pogu" 
try:
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='expand']")))
    more_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

sleep(3)



# Spiež "Show Transcript pogu" 
try:
    show_transcript = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primary-button']/ytd-button-renderer/yt-button-shape/button")))
    show_transcript.click()
except Exception as e:
    print(f"An error occured: {e}")


sleep(3)



# Atrod transkripta logu un nokopē visu tekstu 

transcript_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='body']/ytd-transcript-segment-list-renderer")))
transcript = transcript_element.text
print(transcript)


# Pieļaujam, ka transkripts ir string rinda ar laika norādi un tekstu.

# Sagrupē rindas kopā kā laika norāde un teksta pāros

lines = transcript.strip().split('\n')

# Sagrupē rindas (timestamp, text) pāros
transcript_pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]


file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

# Saglabā šīs rindu pārus CSV failā
if file_path:
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Text"])  # Uzraksta kolonnas virsrakstus Timestamp un Text
        writer.writerows(transcript_pairs)  # Pieraksta laika norādes un teksta rindas

# Piedāvā saglabāt excel formātā
prompt_for_excel = messagebox.askyesno(title="Apstiprinājums", message="Vai Jūs vēlaties saglabāt transkriptu arī Microsoft Excel formātā?")

if prompt_for_excel:
    transcript_sadalits = transcript.split('\n')
    transcript_timestamps = transcript_sadalits[::2]

    transcript_text = transcript_sadalits[1::2]
    df = pd.DataFrame({'timestamp':transcript_timestamps,'text':transcript_text})
    
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")

    if file_path:
        # Saglabā DataFrame Excel failī
        df.to_excel(file_path, index=False)

        messagebox.showinfo(title="Apstiprinājums", message="Fails saglabāts excel formātā.")


# Apstiprinājuma logs
end_window_resultbox = messagebox.showinfo(title="Apstiprinājums", message="Transkripts veiksmīgi saglabāts.")
