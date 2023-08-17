from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")
time.sleep(5)
titles = driver.find_elements(By.CSS_SELECTOR, '[class="ContentTitle__title--e3qXt"]')

for title in titles:
    print(title.text)
# 10초 동안 현재 상태에서 대기
time.sleep(10) 