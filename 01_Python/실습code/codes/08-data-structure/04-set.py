# set : 순서와 중복이 없는 변경가능한 자료형

# s.add(x) : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음.
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4) 
print(my_set)  # {'c', 2, 3, 1, 'a', 4, 'b'}

my_set.add(4)
print(my_set)  # 이미 존재하여 변화 없음

# clear() : 세트 s의 모든 항목을 제거
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # set()


# remove() : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 KeyError

my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)  # {1, 3, 'a', 'c', 'b'}
# my_set.remove(10)
# print(my_set)  # KeyError

# s.pop() : 세트 s에서 임의의 항목을 반환하고, 해당 항목을 제거

my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # a
print(my_set) # {2, 3, 1, 'c', 'b'}

# s.discard(x) : 세트 s에서 항목 x를 제거

my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)  # {'c', 'a', 1, 'b', 3}

my_set.discard(10)
print(my_set)  # 에러가 나진 않는다.

# s.update(iterable) : 세트 s에 다른 iterable 요소를 추가

my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # {1, 2, 3, 4, 5, 'a', 6, 'b', 'c'}

# 세트 집합 메서드

set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0 , 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))   #  True
print(set1.issuperset(set2))  #  False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}