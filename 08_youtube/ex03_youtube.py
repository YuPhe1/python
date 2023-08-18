from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

# driver.maximize_window()    # 창 크기 최대로

time.sleep(2)
# wait = WebDriverWait(driver, 20)

# selenium으로 javascript 적용하기
# excute_script(): javascript 코드를 실행해주는 코드
# h1: 처음 페이지를 열었을 때 높이 값
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print("처음높이:",h1)
# 스크롤을 현재높이 만큼 내리기
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
# 영상 로딩 시간
time.sleep(2)
# 스크롤 내린뒤 높이값
h2 = driver.execute_script("return document.documentElement.scrollHeight")
print("두번째 높이:",h2)



driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
time.sleep(2)
h3 = driver.execute_script("return document.documentElement.scrollHeight")
print("두번째 높이:",h3)