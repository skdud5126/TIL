# 실습 (2, 8, 16진수로 표현해보기)

def conversion(num, decimal ):
    res = []
    while num!=0:
        res.append(num%decimal)
        num//=decimal
    res.reverse()
    res_fin.append(''.join(map(str,res)))
    return res_fin

num = int(input())

li = [2, 8, 16]  # 진수 목록
res_fin = []  # 2, 8, 16진수 나타낼 목록
for i in range(len(li)):
    conversion(num, li[i])

# print(*res_fin)

for de in range(len(res_fin)):
    print(f'{li[de]}진수 : {res_fin[de]}', end =' / ')