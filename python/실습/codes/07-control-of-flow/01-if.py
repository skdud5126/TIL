# 제어문 : 코드의 실행 흐름을 제어하는 데 사용되는 구문
# 조건문 : 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

a = 3

if a > 3:
    print('3 초과')
else:
    print('3 이하')

dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')