from itertools import permutations
import sys
# 인코딩
sys.stdin = open('real_input.txt', 'r', encoding='UTF8')

def calcul_score(): # 플레이어들 점수 계산하는 함수
    player_score = [] # 플레이어들 점수 저장
    # 영어로 타자 쳤을 때와 한글로 타자 쳤을 때 다르게 저장
    for i in range(0,N*2):
        if array[i][2] == 'E':
            score = int(array[i][0]) * (int(array[i][1]) / 100)
            player_score.append(int(score))
        else:
            score = int(array[i][0]) * (int(array[i][1]) / 100) * 0.7
            player_score.append(int(score))
    return player_score


def final(): # 팀점수 평균과 팀원 이름 저장하는 함수
    score_array = calcul_score()
    team_status = [] # 평균 점수 및 팀원 저장
    for i in range(0,N*2,2):
        team = []
        final_score = (score_array[i]+score_array[i+1]) // 2
        player1 = array[i][3]
        player2 = array[i+1][3]
        team.append(final_score)
        team.append(player1)
        team.append(player2)
        team_status.append(team)
    return team_status


def real_final(): # 팀의 원점수의 자리수 바꾸면서 강사님 점수와 비교하여 가장 적은 점수 차 구하는 함수
    min_score = [] # 팀별 최소 점수 차 저장
    for i in range(N):
        min_v = 10000
        p_score =[] # 순열 저장
        for p in permutations(final_score_list[i]):
            p_score.append(int(''.join(p)))
        for i in range(len(p_score)):
            score = abs(teacher_score - p_score[i]) # 점수 차
            if min_v > score:
                min_v = score
        min_score.append(min_v)

    return min_score


N = int(input())
S,P = map(int, input().split())
array = [list(input().split()) for _ in range(N*2)]
teacher_score = int(S * (P / 100)) # 강사님 점수 정보
answer = final() # 점수와 팀원 이름 정보
# print(answer)

final_score_list = [] # 팀 점수 평균 저장
for i in range(N):
    if answer[i][0] < 100: # 2자리일때는 0 추가해서 3자리 만들기
        score = str(answer[i][0] * 10)
        final_score_list.append(score)
    else:
        final_score_list.append(str(answer[i][0]))

result = real_final() # 최종 점수차
real_result = []
for i in range(N):
    real_result.append([result[i],answer[i][0]])

# a = calcul_score()
# print(a)
# print(real_result)

team_name_score = sorted(enumerate(real_result), key = lambda x:(x[1][0], -x[1][1]))
# 점수 차를 기준으로 내림차순으로 정렬하늗네 같을 경우 원점수를 기준으로 오름차순으로 정렬

# print(team_name_score)


for i in range(N):
    print(f'{i+1}등: {answer[team_name_score[i][0]][1]} {answer[team_name_score[i][0]][2]} ({team_name_score[i][0]+1} )|점수 차: {team_name_score[i][1][0]}|원점수:{team_name_score[i][1][1]}')
