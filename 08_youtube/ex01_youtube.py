from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

time.sleep(2)

# 제목요소 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
for title in titles:
    # print(title.text) # innerHTML 값
    # print(title.tag_name) # 해당 요소의 태그 이름
    print(title.get_attribute("aria-label")) # 해당 요소의 aria-label 속성값 가져오기