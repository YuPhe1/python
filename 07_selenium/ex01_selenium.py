from selenium import webdriver
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome();
# 접속할 주소
driver.get("https://www.google.com")
# 10초 동안 현재 상태에서 대기
time.sleep(10) # 웹페이지가 다 열리기전에 종료되는 것을 방지
