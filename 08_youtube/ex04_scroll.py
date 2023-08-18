from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

driver.maximize_window()    # 창 크기 최대로

# while문을 적용하여 무한스크롤 구현하기
# while문 내부동작
# 1. 처음 높이값 확인.
# 2. 높이 만큼 스크롤 내리기
# 3. 높이값 확인
# 4. 높이가 같나면 break로 while문 중단
while True:
    # 스크롤 하기 전 높이
    h1 = driver.execute_script("return document.documentElement.scrollHeight")
    # 스크롤
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    time.sleep(3)
    # 스크롤 한 후 높이
    h2 = driver.execute_script("return document.documentElement.scrollHeight")
    #  두 스크롤 값이 같은지 확인
    if h1 == h2:
        print(h1, h2, "종료")
        break