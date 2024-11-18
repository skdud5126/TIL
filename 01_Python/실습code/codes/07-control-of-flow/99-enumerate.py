# enumerate : iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)