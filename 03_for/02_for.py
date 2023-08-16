list1 = [10, 20, 30, 40, 50]
for i in list1:
    print(i, end=" ")

print()

list2 = ["가", "나", "다", "라", "마"]
for i in list2:
    print(i, end=" ")

print()

# 리스트 2개를 동시에 반복분으로 접근하기
for i, j in zip(list1, list2):
    print(i, j)

print()

list3 = ["python", "java", "c", ["javascript", "typescript"]]
for i in list3:
    print(i, end=" ")