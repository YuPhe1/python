from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/feed/trending")

time.sleep(3)

# # 제목요소 가져오기
# titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# for title in titles:
#     if title.get_attribute("aria-label") and title.text: # shorts 영상을 걸러내기 위한 조건문 또는 숨은영상 걸러내기
#         aria_label = title.get_attribute("aria-label")
#         start_index = aria_label.rfind("조회수")+4
#         end_index = aria_label.rfind("회")
#         hits = aria_label[start_index:end_index]
#         hits = int(hits.replace(",",""))
#         print("제목:",title.text)
#         print("조회수:",hits)

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
        if(start_index > 3): # 유튜브 음악 추천 거르기
            hits = aria_label[start_index:end_index]
            hits = int(hits.replace(",",""))
            # print("제목:",title.get_attribute("title"))
            # print("조회수:",hits)
            # 제목, 조회수를 각각 리스트에 담김
            # append(): 리스트에 데이터를 추가할 떼
            title_list.append(title.get_attribute("title"))
            hits_list.append(hits)

# 리스트 데이터 확인
# print("제목 리스트", title_list)
# print("조회수 리스트", hits_list)

# 제목, 조회수 리스트 함께 조회
for title, hit in zip(title_list, hits_list):
    print(title, hit)