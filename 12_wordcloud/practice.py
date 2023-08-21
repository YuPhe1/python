from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv

f = open('result2.csv','r', encoding='UTF8')
rdr = csv.reader(f)

okt = Okt()

word_list = []
# 명사, 형용사만 추출
for text in rdr:
    for word, tag in okt.pos(text[1]):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

icon = Image.open('./12_wordcloud/image.jpg')
plt.imshow(icon)

mask = np.array(icon)

# 워드 클라우드 객체 생성
wc = WordCloud(font_path='./12_wordcloud/NanumGothic.ttf', background_color='white', max_words=300, mask=mask)

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으니 생략
# # 결과를 이미지로 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()