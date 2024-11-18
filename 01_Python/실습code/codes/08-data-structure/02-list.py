# append : 리시트 마지막에 항목 x를 추가

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(5))  # None

# extend : literable m의모든 항목들을 리스트 끝에 추가 ( +=과 같은 기능)

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend(6)
# print(my_list)  literable 항목이 아니기에 Error 만약 넣으려면 리스트형태로 [6]

my_list.append([9, 9, 9])
print(my_list) # [1, 2, 3, 4, 5, 6, [9, 9, 9]]

# insert : 리스트 인덱스 i 항목 x를 삽입

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # [1, 4, 2, 3]

# remove : 리스트 가장 왼쪽에 있는 항목(첫번째)x를 제거 항목이 존재하지 않을 경우, ValueError

my_list = [1, 3, 2, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# pop : 리스트 가장 오른쪽에 있는항목(마지막)을 반환 후 제거
# pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거


my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()  
item2 = my_list.pop(1)

print(item1)  # 5
print(item2)  # 2
print(my_list) # [1, 3 4]


# clear : 리스트의 모든 항목 삭제

my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []


# index : 리스트에서 첫 번째로 일치하는 항목x의 인덱스를 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
print(my_list.index(1))  # 0

# count : 리스트에서 항목 x의 개수를 반환
my_list = [1, 2, 3, 3, 3, 3]
count = my_list.count(3)
print(count)  # 4


# reverse : 리스트의 순서를 역순으로 변경(정렬X)
my_list = [1, 3, 2, 5, 4]
my_list.reverse()
print(my_list)  # [4, 5, 2, 3, 1]
print(my_list.reverse()) # None


# sort : 리스트를 정렬

my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)

my_list.sort(reverse= True)
print(my_list)  # [100, 3, 2, 1]