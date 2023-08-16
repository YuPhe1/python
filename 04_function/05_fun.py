# 실행하면 콘솔에서 1또는 2를 입력받고 1은 세로형구구단,
# 2는 가로형 구구단을 각각 출력한다.
# 구구단을 각각 함수로 정의한다.
def ymul():
    for i in range(2,10):
        for j in range(1,10):
            print(i, 'x', j, '=', i*j)

def xmul():
    for i in range(2,10):
        print(i, "단", sep="")
        for j in range(1,10):
            print(i, 'x', j, '=', i*j, end = "  ")
        print()

def ymul2(n):
    for i in range(1,10):
        print(n, 'x', i, '=', n*i)

def xmul2(n):
    print(n, "단", sep="")
    for i in range(1,10):
        print(n, 'x', i, '=', n*i, end = "  ")

def inputS(inStr):
    value = int(input(inStr))
    return value

inNum = inputS("1또는 2를 입력하세요: ")
if inNum == 1:
    ymul()
elif inNum == 2:
    xmul()
else:
    print("1또는 2를 입력해 주세요")

n = inputS("몇단을 출력하시겠습니까?: ")
if inNum == 1:
    ymul2(n)
elif inNum == 2:
    xmul2(n)