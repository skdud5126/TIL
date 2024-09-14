# 내장 함수(built-in-func) : 파이썬이 기본적으로 제공하는 함수

numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse = True))  # [5, 4, 3, 2, 1]

# map - 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

numbers = [1, 2, 3]
result = map(str,numbers)
print(result)
print(list(result))

# numbers1 = input().split()
# print(numbers1)

# numbers2 = list(map(int, input().split()))
# print(numbers2)


# zip : 임의의 iterable을 모아튜플을 원소로 하는 zip object를 반환

girls = ['jane', 'ashely']
boys = ['peter','jay']
pair = zip(girls, boys)

print(pair)
print(list(pair))

kr_scores = [10, 20, 30, 50]
mt_scores = [20, 40, 50]
en_scores = [40, 20, 30, 50]

for students_scores in zip(kr_scores, mt_scores, en_scores):
    print(students_scores)

# zip활용 : 2차원 리스트의 같은 컬럼 요소를 동시에 조회할 때

scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50]
]

for score in zip(*scores):
    print(score) 