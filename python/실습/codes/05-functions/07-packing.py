# Packing : 여러 개의 값을 하나의 변수에 묶어서 담는 것

packed_values = 1, 2, 3, 4, 5
print(packed_values)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5 

def my_func(*objects) :
    print(objects)
    print(type(objects))


my_func(1, 2, 3, 4, 5)