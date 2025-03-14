# dict : key-value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

my_dict_1 = {}
my_dict_2 = {'key' : 'value'}
my_dict_3 = {
    'apple' : 12,
    'list' : [1, 2, 3]
}


print(my_dict_1)  # {}
print(my_dict_2)  # {'key' : 'vlaue'}
print(my_dict_3)  # {'apple' : 12, 'list' : [1, 2, 3]}


my_dict = {
    'apple' : 12,
    'list' : [1, 2, 3]
}


# 딕셔너리는 키에 접근해 값을 얻어냄
print(my_dict['apple'])

# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple' : 12, 'list' : [1, 2, 3], 'banana' : 50}

# 변경
my_dict['banana'] = 1000
print(my_dict)  # {'apple' : 12, 'list' : [1, 2, 3], 'banana' : 1000}

