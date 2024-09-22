'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 전위 순회 구현(나 -> 왼쪽 -> 오른쪽) : 이진트리일때만 가능

def preorder(node):
    if node == 0:
        return
    
    print(node, end = ' ')  # 본인을 먼저 확인
    preorder(left[node])  # 왼쪽을 보고나서, 본인을 확인
    preorder(right[node])  # 왼쪽, 오른쪽 자식들을 모두 보고나서, 본인을 확인



# left, right를 쓰는 버전

N = int(input())  # 정점의 개수(정점: 1 ~ N 번)
arr = list(map(int, input().split()))

left = [0] * (N+1) # 왼쪽 자식 번호를 저장할 리스트
# ex) left[3] = 2 ==> 3번 부모의 왼쪽 자식은 2다.

right = [0] * (N+1) # 오른쪽 자식 번호를 저장할 리스트

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]

    # 왼쪽 자식이 없다면, 왼쪽에 삽입
    if not left[parent]:
        left[parent] = child
    # 왼쪽 자식은 있는데, 오른쪽 자식이 없다면 오른쪽에 삽입
    else:
        right[parent] = child

# print(left)
# print(right)

root = 1 # 시작점은 1이다라고 가정.
preorder(root)