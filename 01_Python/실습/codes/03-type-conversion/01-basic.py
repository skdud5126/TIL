# 암시적 형변환 : 파이썬이 자동으로 수행하는 형변환

print(3 + 5.0)  # 8.0
print(True + 3)  # 4
print(True + False) # 1

# 명시적 형변환 : 프로그래머가 직접 지정하는 형변환 암시적 형변환이 아닌 경우를 모두 포함

print(int('1'))
# print(int('3.5'))  # valueError
print(int(3.5))  # 소숫점 버림
print(float('3.5'))  # 3.5

print(str('3') + '등')  # 3등