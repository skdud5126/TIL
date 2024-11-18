# List Comprehension : 간결하고 효율적인 리스트 생성 방법

# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

# 사용 후

nunmbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]

print(squared_numbers)

# 활용 예시 - 2차원 배열 생성시

data1 = [[0]*(5) for _ in range(5)]
print(data1)

# 또는

data2= [[0 for _ in range(5)] for _ in range(5)]
print(data2)