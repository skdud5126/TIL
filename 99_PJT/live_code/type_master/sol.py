import sys
sys.stdin = open('real_input.txt',  'rt', encoding='UTF8')

import itertools

# 입력 받기
N = int(input())  # 팀의 수
S, P = map(int, input().split())  # 강사의 점수와 정확도

teams = []  # 팀 정보를 담을 리스트
for _ in range(N):
    scores = []
    for _ in range(2):
        score, accuracy, language, name = input().split()
        score = int(score)
        accuracy = int(accuracy)
        if language == 'K':  # 한글 타자인 경우 점수에 0.7을 곱함
            score *= 0.7
            score = int(score)
        scores.append((score * accuracy // 100, name))  # 정확도에 따라 점수를 계산하여 리스트에 추가
    teams.append(scores)

# 강사의 점수 계산
S = S * P // 100

# 각 팀의 점수 평균과 강사와의 차이 계산
team_results = []
for idx, team in enumerate(teams):
    team_avg = sum([score[0] for score in team]) // 2
    diff = abs(team_avg - S)    # 원점수
    perms = list(itertools.permutations(str(team_avg).zfill(3), len(str(team_avg).zfill(3))))
    min_diff = min(abs(S - int(''.join(p))) for p in perms)
    team_results.append((idx + 1, team_avg, team_avg, min_diff))

# 결과 정렬 및 출력
team_results.sort(key=lambda x: (x[3], -x[2]))  # 강사와의 차이가 작은 것부터 정렬, 같은 경우에는 원래 점수가 높은 팀이 우선순위
for idx, result in enumerate(team_results, 1):
    print(f'{idx}등 : {teams[result[0]-1][0][1]} {teams[result[0]-1][1][1]} ({result[0]} 팀) | 점수 차 : {result[3]} | 원점수 : {result[2]}')
