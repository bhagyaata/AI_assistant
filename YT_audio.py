

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class Music:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def play(self, query):
        search_url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
        self.driver.get(search_url)

        time.sleep(3)

        try:
            video = self.driver.find_element(By.XPATH, '//*[@id="dismissable"]')
            video.click()
        except Exception as e:
            print("Error finding or clicking the video:", e)



