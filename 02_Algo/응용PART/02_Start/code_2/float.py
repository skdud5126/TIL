t = 0.1
print(f'{t:.20f}')


# 비트로 표현하면 무한 반복되는 숫자끼리 더하기 때문에
# 오차가 발생한다!
print(0.1 + 0.1 == 0.2)  # True : 오차가 허용범위 안이다
print(0.1 + 0.1 + 0.1 == 0.3)  # False : 오차가 허용범위 밖이다

