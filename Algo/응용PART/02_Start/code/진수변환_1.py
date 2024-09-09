# 10진수로 형변환

print(int('10'))

# 2진수, 8진수, 16진수로 변환
print(bin(10))  # 0b1010  : 문자열로 표기된다는 점! 
print(type(bin(10)))  # <class 'str'>

print(oct(10))  # 0o12  : 8진수
print(hex(10))  # 0xa  : 16진수

# 16진수 -> 10진수
print(int('F', base = 16))  # 15
print(int('1010', base = 2))  # 10

print(bin(8)[2:])  # 4bit로 표기 -> 전처리 : 1000
print(bin(1)[2:].zfill(4))   # 0001

for i in range(16):
    print(bin(i)[2:].zfill(4))


bin_to_hex = {}

for i in range(16):
    print(bin(i)[2:].zfill(4))
    print(hex(i)[2:])
    print(f'16진수 변환 소문자: {i:x}')  # 16진수 변환 소문자: f
    print(f'16진수 변환 대문자: {i:X}')  # 16진수 변환 대문자: F
    print(f'2진수 변환: {i:04b}')        # 2진수 변환: 1111
    bin_to_hex[f'{i:04b}'] = f'{i:X}'

print(bin_to_hex)

'''
bin_to_hex = {
                '0000': '0', 
                '0001': '1', 
                '0010': '2', 
                '0011': '3', 
                '0100': '4', 
                '0101': '5', 
                '0110': '6', 
                '0111': '7', 
                '1000': '8', 
                '1001': '9', 
                '1010': 'A', 
                '1011': 'B', 
                '1100': 'C', 
                '1101': 'D', 
                '1110': 'E', 
                '1111': 'F'
                }
'''

hex_to_bin_2 = {f'{i:X}' : f'{i:04b}' for i in range(16)}
print(hex_to_bin_2)