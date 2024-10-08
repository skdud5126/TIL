'''
11011110
11011
'''

print(0b11011110 & 0b11011)
print(bin(0b11011110 & 0b11011))

'''
0x4A3 | 25
'''

print(0x4A3 | 25)
print(bin(0x4A3), bin(25))
print(bin(0x4A3|25))


print('--------------------------')

print(1)
print(1 << 1)  # 2 (10₂)
print(1 << 2)  # 4 (100₂)
print(1 << 3)  # 8 (1000₂)
print(1 << 4, bin(1 << 4))  # 16

print(7 >> 2, bin( 7 >> 2))  # 7(111₂)

print('--------------------------')

arr = [1, 2, 3, 4]

# 각 자리를 쓴다/안 쓴다 - > 나올 수 있는 경우의 수 = 2가지
# 각 자리마다 2가지의 경우의 수 - > N 길이라면 - > 2^N만큼의 경우의 수가 나올 수 있다.
print(f'부분집합의 수 : {1 << len(arr)}')

for i in range(1 << len(arr)):
    print(i, end = ' ')
print()


print('--------------------------')


# i & (1 << N) : N번째 비트가 0인지 아닌지 알 수 있다.


# i 의미 : i번째 부분집합

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # i & (1 << idx)
        # - i번째 부분집합에 idx 요소가 포함되어 있나요?
        if i & (1 << idx):
            print(arr[idx], end = ' ')
    print()


print('--------------------------')

print(bin(4))
print(bin(~4))
print(~4)