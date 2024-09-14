# range : 연속된 정수 시퀀스를 차례로 생성하는 변경 불가능한 자료형

my_range_1 = range(5)
my_range_2 = range(1, 10)
print(my_range_1)  # my_range(0, 5)
print(my_range_2)  # my_range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 주로 반복문과 함께 활용
for i in range(5):
    print(i)

for j in range(1,11,2):
    print(j)