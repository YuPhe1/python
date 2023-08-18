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



# 스크롤 후 제목데이터를 리턴하는 함수
def scroll_fun():
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
    # 제목 가져오기
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return titles        
# 무한 스크롤 함수 호출
titles = scroll_fun()


for title in titles:
    print(title.text)
print("영상 갯수:", len(titles))