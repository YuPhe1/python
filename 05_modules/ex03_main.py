# 구구단 함수를 ex03_function.py 에 각각 정의하고
# main에서 1,2 번 선택을 받아 세로형, 가로형을 가각
# 출력할 수 있도록 하시오.
from ex03_function import *

run = True
while run:
    sel = int(input("선택: "))
    if sel == 1:
        fun1()
    elif sel == 2:
        fun2()
    else:
        print("종료")
        run = False