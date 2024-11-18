# 람다함수 : 익명 함수를 만드는데 사용되는 표현식

# 함수
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result)  # 8

# 람다 함수 
lambda x,y : x + y

# with map 함수

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# Lambda 미사용
squared_1 = list(map(square, numbers))
print(squared_1)  # [1, 4, 9, 16, 25]

# Lambda 사용
squared_2 = list(map(lambda x : x**2, numbers))
print(squared_2)