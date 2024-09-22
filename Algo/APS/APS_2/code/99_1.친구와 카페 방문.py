friends = ['A', 'B', 'C', 'D', 'E']

def get_sub(friends):
    cnt = 0
    for i in range(len(friends)):
        if friends & 0x1:
            cnt += 1
        friends >>= 1
    return cnt

result =0
for friend in range(1 << len(friends)):
    if get_sub(friends) >= 2:  # bit가 2이상 1이라면
        result +=1
print(result)