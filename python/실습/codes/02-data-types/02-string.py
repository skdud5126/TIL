# Sequence Types(str, list, tuple, range) - 여러 개의 값들을 순서대로 나열하여 저장하는 자료형

# Hello, world!
print('Hello, world!')

# str
print(type('Hello, world!'))

# Escape sequence : 역슬래시(backslash) 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
print('철수야 \'안녕\'')
print('이 다음은 엔터\n입니다.')

# f-string
bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')


my_str = 'Hello'

# 인덱싱
print(my_str[1])  # e

# 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # Hel
print(my_str[3:])  # lo
print(my_str[0:5:2])  # Hlo
print(my_str[::-1])  # olleH

# 길이
print(len(my_str))  # 5

# 문자열은 변경 불가능한 시퀀스 자료형
my_str[1] = 'z'

