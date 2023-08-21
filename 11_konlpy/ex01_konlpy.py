from konlpy.tag import Kkma
from konlpy.tag import Okt

# Kkma 모듈 객체 선언
kkma = Kkma()

# 형태소 단위로 뽑아내기
print(kkma.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# 명사만 뽑아내기
print(kkma.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# 형태소 단위로 뽑아내 품사 정보와 함께 담아내기
# 태그정보
# http://kkma.snu.ac.kr/documents/index.jsp?doc=postag
print(kkma.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))


okt = Okt()

print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(okt.normalize(u'안녕하세욬ㅋㅋㅋ'))

text = "안녕하세요. 파이썬 입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재밌습니다."
# 단어와 종류를 분리
for word, tag in kkma.pos(text):
    print(word, tag)
for word, tag in okt.pos(text):
    print(word, tag)
