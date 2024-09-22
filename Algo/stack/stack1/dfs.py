# DFS 예시

# graph: 그래프를 나타내는 인접 리스트
# start: 탐색을 시작할 정점
# visited: 방문한 정점을 저장하는 집합
# res: 탐색 경로를 저장하는 리스트

def dfs(graph, start, visited, res):
    visited.add(start)  # 방문 표시
    res.append(start)  # 현재 정점을 탐색 경로에 추가

    for neighbor in graph[start]:  # 현재 정점의 모든 인접 정점에 대해
        if neighbor not in visited: # 인접 정점이 아직 방문되지 않았다면
            dfs(graph, neighbor, visited, res) # 그 정점으로 DFS 재귀 호출


# 그래프 인접 리스트
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'G'],
    'D' : ['B', 'F'],
    'E' : ['B', 'F'],
    'F' : ['D', 'E', 'G'],
    'G' : ['C', 'F']
}

start = 'A'
# set 중복이 없고 특정 원소가 set에 포함되어 있는 지 확인하는 과정이 시간복잡도 O(1)
# 리스트는 포함되어 있는 평소 유무를 확인하는데 시간복잡도 O(N)
visited = set()
res = []

dfs(graph, start, visited, res)

print(*res)


"""
인접행렬
    adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬
    for _ in range(E):
        v, w = map(int, input().split())    # v출발, w 도착 (유향그래프)
        adjM[v][w] = 1                      # v에 인접한 w
        #adjM[w][v] = 1                      # 무향그래프였다면
        
인접리스트
    adjL = [[] for _ in range(V+1)]         # 인접 리스트
    for _ in range(E):
        v, w = map(int, input().split())    # v출발, w 도착 (유향그래프)

        adjL[v].append(w)
"""
