'''
4 5
00110
00011
11111
00000

3 3
001
010
101
'''

def dfs(x, y):
    
    for dx, dy in dxy:
        nx, ny = x + dx, y+dy
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if visited[nx][ny]== 0 and arr[nx][ny]=='0':
            visited[nx][ny]==1  # 방문 표시
            dfs(nx,ny)


    # if visited[x][y]==0 and arr[x][y]=='0':
    #     visited[x][y]==1



N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]

dxy = [[0,1], [1,0], [0,-1], [-1,0]]
ans=0

for i in range(N):
    for j in range(M):

        if arr[i][j] == '0':
            visited[i][j]=1
            dfs(i,j)
            ans+=1

print(ans)
