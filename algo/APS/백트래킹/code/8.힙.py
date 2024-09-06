# from heapq import heappush, heappop

# arr = [20, 15, 19, 4, 13, 11]

# # 최소힙
# min_heap = []

# for el in arr:
#     heappush(min_heap, el)

# print(min_heap)  # [4, 13, 11, 20, 15, 19] 출력

# while len(min_heap) > 0:
#     print(heappop(min_heap), end=' ')

# print()

# # 최대힙
# max_heap = []
# for el in arr:
#     heappush(max_heap, -el)

# print(max_heap)  # [-20, -15, -19, -4, -13, -11] 출력

# while len(max_heap) > 0:
#     print(-heappop(max_heap), end=' ')

def enq(n):
    global last
    last +=1
    h[last] = n
    c = last
    p = c//2
    while p>=1 and h[p] < h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2



N = int(input())
arr = list(map(int,input().split()))

h = [0] * (N+1)
last = 0

for num in arr:
    enq(num)

print(h)