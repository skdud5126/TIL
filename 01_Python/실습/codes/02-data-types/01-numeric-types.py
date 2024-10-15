print(2 / 3)   # 0.66666666666
print(5 / 3)   # 1.66666666667

# 부동 소수점 문제
# - 컴퓨터가 실수를 표현하는 방식으로 인해 발생하는 작은 오차
#   - 원인 : 실수를 2진수로 변환하는 과정에서 발생하는 근사치 표현

a = 3.2 - 3.1
b = 1.2 - 1.1

print(a)
print(b)

# 부동 소수점 해결
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)
print(b)
print(a == b)

# 314 * 0.01
number = 314e-2

# 3.14
print(number)

# float
print(type(number))