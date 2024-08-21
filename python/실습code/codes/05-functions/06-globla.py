# global 키워드 : 변수의 스코프를 전역 범위로 지정하기 위해 사용
# 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 이용

num = 0 #  전역 변수

def increment():
    global num
    num += 1

print(num)  # 0

increment()

print(num)  # 1