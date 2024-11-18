# 튜플 : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuole_3 = (1, 'a', 3, 'b', 5)

my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[0:5:2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5

# TypeError : 'tuple' object does not support item assignment
# my_tuple[1] = 'z'


# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
print(x)
print(y)

x, y = (100, 200)
print(x, y)