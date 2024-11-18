# 매개변수 : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
# 인자 : 함수를 호출할 때, 실제로 전달되는 값

def add_numbers(x,y) : # x와 y는 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a,b)  # a,b는 인자
print(sum_result)

# 1. 위치인자(Positional Arguments) : 함수 호출 시 인자의 위치에 따라 전달되는 인자

def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살 이시군요.')

print('위치 인자 출력 값')
greet('Alice', 30)
greet(25, 'Dany')  # 위치인자는 순서가 중요하다는 점


# 2. 기본 인자 값(Default Argument Values) : 함수 정의에서 매개변수에 기본 값을 할당하는 것

def greet(name, age = 30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

print()
print('기본 인자 출력 값')
greet('Alice')
greet('Dan', 20)

# 3. 키워드 인자(Keyword Arguments) : 함수 호출시 인자의 이름과 함께 값을 전달하는 인자
# 매개변수와 인자를 일치키시지 않고, 특정 매개변수에 값을 할당 할 수 있음

def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

print()
print('키워드 인자 출력값')
greet(age = 24, name ='Alice')
greet('Dave', age=30)  # 키워드 인자는 위치 인자 뒤에 위치


# 4. 임의의 인자 목록(Arbitrary Argument Lists) : 정해지지 않은 개수의 인자를 처리하는 인자
# 여러 개의 인자를 tuple로 처리(파이썬이 내부적으로 동작할 때 사용하기 때문)

def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

'''
(1, 2, 3)
합계 : 6
'''
print()
print('임의의 인자 목록 출력 값')
calculate_sum(1, 2, 3)

# 5. 임의의 키워드 인자 목록(Arbitary Keyword Argument Lists) : 정해지지 않은 개수의 키워드 인자를 처리하는 인자 
# 여러 개의 인자를 dictionary로 묶어 처리

def print_info(**kwargs):
    print(kwargs)

print_info(name = 'Eve', age = 30)