# while : 주어진 조건식이 참인 동안 코드를 반복해서 실행

a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

'''
0
1
2
끝
'''

number = int(input('양의 정수를 입력하세요 : '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')