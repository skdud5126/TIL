# 함수: 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

def make_sum(param1, param2):
    return param1 + param2

result = make_sum(100, 200)
res = print(result)
print(res)  # None

'''
'''
def make_sum(param1, param2):
    return param1 + param2

result = make_sum(100, 30)
return_value = print(result)
print(return_value)

# print 자체는 단순히 결과를 보여주기만 함. 아무런 값 반환하는 것 아님
# return은 함수가 실행되었을때 그 결과를 반환.

