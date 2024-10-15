# row : 현재 퀸을 놓을 항
# board : 퀸들의 위치를 나타내는 n*n 보드

def is_valid_pos(board, row, col):
    # 현재 열에 다른 퀸이 있는지 검사
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # 대각선 검사를 해야한다.
    '''
    row = col = 2
    range(2, -1, -1)  => [2, 1, 0]
    => for i in zip([2, 1, 0], [2, 1, 0])
    zip 함수 뭐죠? 리스트 2개를 병렬로 묶는다.
    [2, 2], [1, 1], [0, 0]
    '''
    # 왼쪽 윗 대각선 검사
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # 오른쪽 윗 대각선 검사
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def n_queens(row,board):
    if row == n:
        solutions.append([r[:] for r in board])  # deepcopy 써도됨

    for col in range(n):  # 현재 row 행에서 각 열에 대해 퀸을 놓을 수 있는 검사를 한다.
        if is_valid_pos(board, row, col): # 만약에 놓을 수 있다면?
            board[row][col] = 1
            n_queens(row+1, board)  # 다음 행으로 이동하여 재귀호출
            board[row][col] = 0  # 없었던 일로 만든다.


n = 4 # 4개의 퀸을 놓자!
board = [[0] * n  for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트

# dfs다!
# 호출을 중단시킬 파라미터 => 각 행에 퀸을 놓을 수 있는 지 확인하고, 마지막 행까지 간다면 전부 놓은 것
# 우리가 원하는 누적값 :  마지막 행까지 놓였을 때의 체스판 저장 상태를 원한다.

n_queens(0, board)