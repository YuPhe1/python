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

# 카카오 웹툰 태그크롤링

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
tag_list = []
title_list = []
url = "https://page.kakao.com/menu/10010/screen/52?tab_uid="
for i in range(1, 8):
# 접속할 주소
    driver.get(url + str(i))

    time.sleep(1)
    scroll_fun()

    webtoons = driver.find_elements(By.CSS_SELECTOR, 'div.w-full.overflow-hidden div div div a')

    for webtoon in webtoons:
        link = webtoon.get_attribute('href')
        driver.execute_script('window.open("https://google.com")')  #구글 창 새 탭으로 열기
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
        driver.get(link)
        time.sleep(2)
        try:
            title = driver.find_element(By.XPATH ,'//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/span')
            tag = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[1]/div[1]/span[4]')
            text = tag.text
            print(text)
            if title not in title_list:
                title_list.append(title)
                tag_list.append(text)
        except NoSuchElementException:
            print('없음')
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
plt.show()

wc.to_file('kakao_result.jpg')

