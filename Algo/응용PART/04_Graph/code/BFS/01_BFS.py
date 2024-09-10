def bfs(node):
    q = [node]  # 선입선출 구조인 Queue 처럼 활용할 것이다.

    # q에 저장되는 데이터 : 다음에 처리할 데이터(후보군)
    while q:  # 갈 수 있는 곳이 없을 때까지
        now = q.pop(0)  # 가장 앞에 있는 데이터를 뽑는다.
        print(now, end = ' ')  # 현재 노드 출력


        # 현재 정점에서 인접한 정점들을 확인
        for next_node in graph[now]:
            if visited[next_node]:  # 이미 방문한 정점이면 통과
                continue

            visited[next_node] = 1  # 방문처리
            q.append(next_node)    # 후보군에 추가(순서가 되면 처리해주세요.)



# 그래프를 만드는 코드는 DFS와 BFS가 똑같다
# 핵심 : 무슨 노드를 먼저 탐색할 것인가!
#   - 갈 수 있으면 끝까지 가자 : DFS
#   - 특정 정점을 기준으로 퍼져나가면서 확인하자 : BFS

N, M = map(int, input().split())

# 비어있는 리스트를 N+1번 반복하면서 생성
# 1. 비어있는 리스트 : 아직 갈 수 있는 곳이 없다.
# 2. N + 1번 : 0번 인덱스를 버린다. (문제에서 노드번호가 1번부터 시작)
#  # --> 인접리스트를 만들기 위해 아래와 같이 정의
graph = [[] for _ in range(N+1)]

# graph = [[0] * (N+1) for _ in range(N+1)]  #인접행렬 예시

visited = [0]*(N+1)

# 연결 정보를 저장

for _ in range(M):
    s, e = map(int,input().split())

    # 양방향 그래프이므로, 시작 <-> 끝점을 바꾸면서 저장

    graph[s].append(e)
    graph[e].append(s)  # 문제가 방향 그래프라면, 바꾼 정보를 저장하면 버그난다!

visited[1] = 1  # 방문 처리
bfs(1)
