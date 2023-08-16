# 자바의 scanner처럼 실행 후 콘솔에서 숫자를 입력받아
# 홀수, 짝수를 판별하여 출력하는 코드를 작성하시오.
num = int(input())
if(num % 2 == 0):
    print("짝수")
elif num % 2 != 0:
    print("홀수")
else:
    print("숫자가 아닙니다.")