from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
query = input("검색할 내용>")

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.google.com/")

time.sleep(3)

search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
search.send_keys(query)
search.send_keys(Keys.RETURN)
# 제목 저장을 위한 리스트
time.sleep(2)
title_list = []
while True:
    titles = driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb.MBeuO.DKV0Md')
    for title in titles:
        # print(title.text)
        title_list.append(title.text)
    # 다음 버튼이 없으면 중지
    try:
        next = driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]')
        next.click()
        time.sleep(2)
    except NoSuchElementException:
        break

okt = Okt()
# 명사, 형용사 저장을 위한 리스트
word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

word_list_count = Counter(word_list)

# 워드클라우스가 생성될 이미지 모습
icon = Image.open('./12_wordcloud/image.jpg')
mask = np.array(icon)

wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', width=400, height=400, mask=mask, background_color='white')

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으니 생략
# 결과를 이미지로 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()
time.sleep(5)