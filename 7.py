# 1. 계산기능
print(123 + 123 * 123 /123 - 123)
# 큰 따옴표를 친다 = 컴퓨터가 문자로 인식하게 해준다. 숫자를 쳐도 문자로 인식하기에 숫자는 "" ''(X)
# == 계산 기능을 쓸 때에는 따옴표 X
# 2. 변수
# 변수란 ? 프로그램을 작성하는 사람이 원하는 이름을 붙인 "그릇" 그릇에 원하는 값을 넣어서 사용 가능.
lol = 123
bag = 987
print(bag - lol)
fff = "서예일"
print(fff)
# 3. 반복
# for while
# for 의 뜻은 지정한 값의 열에서 1개씩 꺼내어 그것이 끝날 때까지 반복한다.
#while 의 뜻은 지정한 조건을 만족하고 있는 동안 실행한다.
# 4. 조건 분기
# if else 조건문
for a in range(0, 10+1):
    if a <= 5:
        print("작습니다.")
    else:
        print("큽니다.")
# 5. 함수
def sumtotal(a,b):
    total = 0
    for i in range(a, b + 1):
        total = total + i
        return total
# 6. 모듈 (외부기능)


