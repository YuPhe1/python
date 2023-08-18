from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 유튜브 홈페이지 접속
# 2. 검색어 입력
# 3. 엔터
# 4. 필터클릭
# 5. 조회수 클릭
# 6. 무한 스크롤
# 7. 제목 수집
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
# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

time.sleep(2)
# 검색 요소 접근
search = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력
search.send_keys("아이브")

# 엔터 입력
search.send_keys(Keys.RETURN)

time.sleep(2)
# 필터 버튼 요소 접근
filter = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
# 필터 버튼 클릭
filter.click()

time.sleep(2)

# 조회수 버튼 요소 접근
co = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
co.click()

# 무한 스크롤 함수를 호출하여 제목만 출력
scroll_fun()

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
for title in titles:
    print(title.text)
time.sleep(10)