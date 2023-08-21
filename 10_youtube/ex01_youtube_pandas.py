# 크롤링 결과 판다스로 저장하기
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/feed/trending")

time.sleep(3)

# 제목 저장을 위한 리스트
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

# 제목요소 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
for title in titles:
    if title.get_attribute("aria-label") and title.text: # shorts 영상을 걸러내기 위한 조건문
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))        
        title_list.append(title.get_attribute("title"))
        hits_list.append(hits)

# 제목, 조회수 리스트가 담긴 디셔너리
crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
result.to_csv("./result.csv", encoding="utf-8-sig")