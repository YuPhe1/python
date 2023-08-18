from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
# driver.get("https://www.youtube.com/")

# driver.maximize_window()

wait = WebDriverWait(driver, 20)
# element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search')))

# search = driver.find_element(By.CSS_SELECTOR, 'input#search')
# search.send_keys("뉴진스")

# # 엔터 입력
# search.send_keys(Keys.RETURN)

# search_btn = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# search_btn.click()

# 검색결과 페이지에 바로 접속
driver.get("https://www.youtube.com/results?search_query=뉴진스")

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
for title in titles:
    print(title.text)
time.sleep(10)

# https://www.youtube.com/results?search_query=뉴진스
# https://www.youtube.com/results?search_query=아이브