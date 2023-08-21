# 크롤링 결과 판다스로 저장하기
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

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
driver.get("https://www.youtube.com/results?search_query=뉴진스")

time.sleep(3)

# 제목 저장을 위한 리스트
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

# 무한 스크롤 함수 호출
scroll_fun()

# 제목요소 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
for title in titles:
    # shorts 영상, YouTube 영화, 제목데이터 없는 컨텐츠
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): # shorts 영상을 걸러내기 위한 조건문
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수 값 범위에 따라 분리
        # 조회수 없는 영상은 0으로, 조회수가 1000 미만인 영상은 , 처리 생략
        # 조회수 1,000 이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상
        elif not hits:
            hits = 0
        # 조회수 1,000 미만
        else:
            hits = int(hits)
        # 동일한 제목 영상은 한 번만
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

# 제목, 조회수 리스트가 담긴 디셔너리
crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")
# 조회수를 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result2.csv", encoding="utf-8-sig")