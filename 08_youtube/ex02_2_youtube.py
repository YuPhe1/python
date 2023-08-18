from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 콘솔에서 입력받아 검색
query = input("검색> ")
query.replace(" ", "+")
url = "https://www.youtube.com/results?search_query=" + query

driver = webdriver.Chrome()

driver.get(url)

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
for title in titles:
    print(title.text)
time.sleep(10)