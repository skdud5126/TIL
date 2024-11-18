# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, address):
        super().__init__(name, age, number, email)
        self.address = address

std = Student('김나영', 25, 1111, 'skdud5126@naver.com', 'KOREA')
print(std.name)
print(std.address)


# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'Parent_A'

    def show_value(self):
        print(f'Value form ParnetA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'Parent_B'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()
        print(f'Value ffrom Child: {self.value_c}')

child = Child()
child.show_value()

'''
Value from ParentA : Parent_A
Value form Child : Child
'''