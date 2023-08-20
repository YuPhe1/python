from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

time.sleep(5)

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

# 제목요소 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title-link"]')
for title in titles:
    if title.get_attribute("aria-label"): # shorts 영상을 걸러내기 위한 조건문
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))
        print("제목:",title.get_attribute("title"))
        print("조회수:",hits)


time.sleep(10)