import pandas as pd

scores = pd.DataFrame(
    [
        [96, 76, 60, 85, 80], # java
        [88, 92, 100, 55, 70], # python
        [10, 20, 30, 40, 50] # js
    ]
)
print(scores)

scores = pd.DataFrame(
    [
        [96, 76, 60, 85, 80], # java
        [88, 92, 100, 55, 70], # python
        [10, 20, 30, 40, 50] # js
    ],
    index=["java", "pyhone", "js"]
)
print(scores)

student_number = [1, 2, 3, 4, 5]
scores = pd.DataFrame(
    [
        [96, 88, 10],
        [76, 92, 20],
        [60, 100, 30],
        [85, 55, 40],
        [80, 70, 50],
    ],
    index=student_number
)
print(scores)

scores = pd.DataFrame(
    {
        "java":[96, 76, 60, 85, 80], # java
        "python":[88, 92, 100, 55, 70], # python
        "js":[10, 20, 30, 40, 50] # js
    },
    index=student_number
)
print(scores)

# 딕셔너리 데이터를 DataFrame으로 변환
scores_dict = {
    "java":[96, 76, 60, 85, 80], # java
    "python":[88, 92, 100, 55, 70], # python
    "js":[10, 20, 30, 40, 50] # js
}
scores = pd.DataFrame(scores_dict)
print(scores)