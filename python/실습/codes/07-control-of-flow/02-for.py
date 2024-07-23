# 반복문 : 주어진 코드 블록을 여러번 반복해서 실행하는 구문

# for문 : 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)


# 문자열(시퀀스 자료형) 순회

country = 'Korea'

for char in country:
    print(char)


# range() 순회

for i in range(5):
    print(i)

# 딕셔너리 순회
my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])


for key, value in my_dict.items():
    print(key, value)

# 인덱스로 리스트 순회

numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print(numbers)  # [16, 36, 100, 64, 25]
