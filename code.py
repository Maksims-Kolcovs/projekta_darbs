from selenium import webdriver 

video_url = input("Lūdzu ievietojiet YouTube video url")

selenium = webdriver.chrome()
selenium.get(video_url)
