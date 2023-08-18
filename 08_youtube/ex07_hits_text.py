# 조회수값 추출하기
aria_label = "IVE 아이브 'LOVE DIVE' MV 게시자: starshipTV 1년 전 2분 59초 조회수 228,267,984회"

# rfind(): 매개변수로 전달한 글자의 인덱스 값을 반환
# 해당 변수의 제일 마지막에서 시작하여 찾음
# find(): 매개변수로 전달한 글자의 인덱스 값을 반환
# 해당 변수의 시작지점에서 시작하여 찾음

# 조회수 값의 시작 인덱스 값
start_index = aria_label.rfind("조회수")+4
# 조회수 값의 끝 인덱스 값
end_index = aria_label.rfind("회")

# 조회수 값만 출력
hits = aria_label[start_index:end_index]
print(hits)
print(type(hits))

# 쉼표 제거 후 정수형으로 변환
# replace(): 문자 바꾸기 기능
hits = int(hits.replace(",",""))
print(hits)
print(type(hits))
