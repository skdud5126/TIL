def dfs(current, adj_matrix, visited):  # current 탐색 정점 / adj_matrix: 인접 행렬 / visited : 방문 체크 리스트
    visited[current] = True   # 현재 정점 방문 표시
    
    for i in range(len(adj_matrix)):  # 모든 정점에 대해
        if adj_matrix[current][i] and not visited[i]:  # 현재 정점과 연결되어 있고, 아직 방문하지 않은 정점이라면
            dfs(i, adj_matrix, visited)  # 그 정점을 방문

N = 5  # 정점 수

adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]   # 인접 행렬

# 방문 체크 배열 초기화
visited = [False] * N   # 모든 정점을 아직 방문하지 않았다고 표시

dfs(0, adj_matrix, visited)  # 깊이 우선 탐색 시작
