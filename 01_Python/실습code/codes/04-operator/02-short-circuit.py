# 단축 평가 : 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0