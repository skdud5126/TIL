# 복합 연산자
y = 10
y -= 4
# y = y - 4

print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w) # 3.75

q = 20
q //= 3
print(q)  # 6

# 비교연산자
print(3 > 6)  # False
print(2.0 == 2)  # True
print(2 != 2) # False
print('HI' == 'hi') # False
print(1 == True)  # True


# is 비교 연산자
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 떄문
# 아래 조건은 항상 False이기 때문에 is 대신 ==를 사용해야 한다는 것을 알림
# ==는 동등성, is는 식별성 / 값을 비교하는 ==와 다름

print(2 is 2.0 ) # False
print(1 is True) # False


# 논리 연산자 (and, or, not)
print(True and False)  # False

print(True or False)  # True

print(not True)  #  False

# 논리연산자 & 비교연산자

num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True


