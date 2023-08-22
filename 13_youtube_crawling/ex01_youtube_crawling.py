from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pymysql

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 무한 스크롤 함수
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
            break

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/feed/trending")

time.sleep(3)

# 제목 저장을 위한 리스트
title_list = []
# 조회수 저장을 위한 리스트
hits_list = []

# 무한 스크롤 함수 호출
scroll_fun()

# Okt() 객체 생성
okt = Okt()
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
        # 조회수 글씨가 없는 영상
        elif start_index == 3:
            hits = 0
        # 조회수 1,000 미만
        else:
            hits = int(hits)
        # 동일한 제목 영상은 한 번만
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)
            
conn = pymysql.connect(
    host='127.0.0.1',
    user='user_python',
    password='1234',
    db='db_python',
    charset='utf8mb4' # 한글 처리
)

cur = conn.cursor() # DB 접속
sql = "insert into `table1` (title, hit) values(%s, %s);"
tuple_results = list(zip(title_list, hits_list))
cur.executemany(sql, tuple_results) # 여러개의 데이터를 한번에 집어넣을때 list, tuple 가능

conn.commit()

# 제목, 조회수 리스트가 담긴 디셔너리
crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")
# 조회수를 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result3.csv", encoding="utf-8-sig")

# 명사, 형용사 저장을 위한 리스트
word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 워드클라우스가 생성될 이미지 모습
icon = Image.open('./12_wordcloud/image.jpg')
mask = np.array(icon)

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(5): # 상위 5 개
    words.append(word)
# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
plt.bar(words, counts)
plt.show()

# 워드 클라우드 객체 생성
# wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400)
# 선택한 이미지 모양으로 표현하고 싶을 때
wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400, mask=mask, background_color='white')

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으니 생략
# 결과를 이미지로 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()
