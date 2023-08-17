from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")

# 특정 조건을 만족할 때 까지 대기
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="ContentTitle__title--e3qXt"]')))

# time.sleep(5)
titles = driver.find_elements(By.CSS_SELECTOR, '[class="ContentTitle__title--e3qXt"]')

for title in titles:
    print(title.text)
