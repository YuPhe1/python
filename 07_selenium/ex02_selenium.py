from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.example.com")

# p 태그 요소만 접근하기

# 10초 동안 현재 상태에서 대기
time.sleep(10)

