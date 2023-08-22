from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

# 네이버 웹툰 태그크롤링

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")

time.sleep(1)

webtoons = driver.find_elements(By.CSS_SELECTOR, 'li.DailyListItem__item--LP6_T a.Poster__link--sopnC')

tag_list = []

for webtoon in webtoons:
    link = webtoon.get_attribute('href')
    driver.execute_script('window.open("https://google.com")')  #구글 창 새 탭으로 열기
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
    driver.get(link)
    time.sleep(1)
    tags = driver.find_elements(By.CSS_SELECTOR, 'a.TagGroup__tag--xu0OH')
    for tag in tags:
        text = tag.text[1:]
        tag_list.append(tag)
    driver.close()  #링크 이동 후 탭 닫기
    driver.switch_to.window(driver.window_handles[-1])  #다시 이전 창(탭)으로 이동
    time.sleep(1)
    
tag_list_count = Counter(tag_list)

# 워드클라우스가 생성될 이미지 모습
icon = Image.open('./12_wordcloud/image.jpg')
mask = np.array(icon)

# 워드 클라우드 객체 생성
# wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400)
# 선택한 이미지 모양으로 표현하고 싶을 때
wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400, mask=mask, background_color='white')

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(tag_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으니 생략
# 결과를 이미지로 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()# 워드 클라우드 객체 생성
# wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400)
# 선택한 이미지 모양으로 표현하고 싶을 때
wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400, mask=mask, background_color='white')

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(tag_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으니 생략
# 결과를 이미지로 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()