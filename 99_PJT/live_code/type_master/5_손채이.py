from itertools import permutations
import sys
# 인코딩
sys.stdin = open('real_input.txt', 'r', encoding='UTF8')
def calculate_score(speed, accuracy, language):
    # 기본 점수
    student_score = speed * accuracy // 100

    # 한글 선택
    if language == 'K':
        student_score = student_score * 7 // 10

    return student_score

def min_result(avg_score, t_score):
    str_avg = str(avg_score)        # 형변환

    while len(str_avg) < len(str(t_score)):
        str_avg += '0'

    perms = set(int(''.join(p)) for p in permutations(str_avg))  # 가능한 모든 자릿수 변환 값

    result = avg_score

    for p in perms:
        tmp = abs(p - t_score)

        if result > tmp:
            result = tmp

    best_score = min(perms, key=lambda x: (abs(x - t_score), -x))  # 차이가 최소인 값 중 큰 값 선택
    return result, best_score


N = int(input())  # 팀 수
S, P = map(int, input().split())     # 강사 타자 수 : S, 정확도 : P

score = S * P // 100  # 강사 점수
teams = []

for i in range(N):
    # 팀원 1
    s1, p1, lang1, name1 = input().split()      # 팀원 1 점수, 정확도, 언어, 이름

    score1 = calculate_score(int(s1), int(p1), lang1)       # 팀원 1 점수

    # 팀원 2
    s2, p2, lang2, name2 = input().split()      # 팀원 2 점수, 정확도, 언어, 이름

    score2 = calculate_score(int(s2), int(p2), lang2)       # 팀원 2 점수

    # 팀 평균 점수
    team_avg = (score1 + score2) // 2

    # 강사 점수와 최소 차이 계산
    score_difference, best_score = min_result(team_avg, score)

    # 팀 정보 저장
    teams.append([score_difference, best_score, team_avg, name1, name2, i + 1])     # i = 팀 번호

# 차이 기준 오름차순, 원점수 기준 내림차순 / 내림차순 하려고 -x함
teams.sort(key=lambda x: (x[0], -x[2]))

# 결과 출력
for rank, team in enumerate(teams, start=1):
    score_difference, best_score, original_score, name1, name2, team_num = team
    print(f"{rank}등 : {name1} {name2} ({team_num} 팀) | 점수 차 : {score_difference} | 원점수 : {original_score}")
