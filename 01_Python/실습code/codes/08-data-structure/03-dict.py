# clear : 딕셔너리 D의 모든 키/값 쌍을 제거

person = {'name': 'Alice', 'age' : 25}
person.clear()
print(person)  # {}

# get : 키 K에 연결된 값을 반환(키가 없으면 None을 반환)
# D.get(k, v) : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환

person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country'))  # None
print(person.get('country', 'UnKnown'))  # Unknown


# D.keys() : 딕셔너리 D의 키를 모은 객체를 반환

person = {'name' : 'Alice', 'age' : 25}
print(person.keys())  # dict_keys(['name', 'age'])

for item in person.keys():
    print(item)

# D.values() : 딕셔너리 D의 값을 모은 객체를 반환

person = {'name' : 'Alice', 'age': 25}
print(person.values())  # dict_vlaues(['Alice', 25])

for value in person.values():
    print(value)


# D.items() : 딕셔너리 D의 키/값 쌍을 모은 객체를 반환

person = {'name' : 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

for k, v in person.items():
    print( k, v)

# D.pop(k) : 딕셔너리 D에서 키 K를 제거하고 연결됐던 값을반환(없으면 오류)

person = {'name' : 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name' : 'Alice'}

# D.pop(k, v) : 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 v를 반환)

person = {'name' : 'Alice', 'name' : 25}
# print(person.pop('country')) # keyError
print(person.pop('country', 'NO-KEY'))

# D.setdefault(k) : 딕셔너리 D에서 키 k와 연결된 값을 반환
# k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환

person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country'))  # None
print(person.setdefault('coutry', 'KOREA'))  # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'coutry': 'KOREA'}

# update(other) : other 내 각 키에 대해 D에 있는 키면 D에 있는그 키의 값을 other에 있는값으로 대체. other에 있는각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가


person = {'name': 'Alice', 'age' : 25}
other_person = {'name' : 'Ben', 'country' : 'KOREA'}
person.update(other_person)
print(person)  # {'name' : 'Ben', 'age': 25, 'country' : 'KOREA'}

person.update(age = 100 , country = 'USA')
print(person)  # {'name' : 'Ben', 'age' : 100, 'country' : 'USA'}