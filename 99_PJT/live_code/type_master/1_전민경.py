import sys
sys.stdin = open('real_input.txt', encoding='utf-8')
from itertools import permutations

# 팀 수 입력
N = int(input())

# 강사 점수와 정확도 입력
kang_s, kang_a = map(int, input().split())

# 학생 데이터를 저장할 빈 리스트 초기화
team_data = []

# 2*N번 입력을 받기 위한 반복문
for _ in range(2 * N):
    # 입력받은 데이터를 공백으로 나누어 리스트로 변환
    student_info = input().split()
    # 변환된 학생 정보를 team_data 리스트에 추가
    team_data.append(student_info)


# 점수 계산 함수
def compute_score(speed, accuracy, language):
    if language == 'K':
        return int(speed * (accuracy / 100) * 0.7)
    return int(speed * (accuracy / 100))


# 팀 점수 계산 및 정렬
def calculate_team_scores(N, kang_s, kang_a, team_data):
    kang_score = int(kang_s * (kang_a / 100))  # 강사 점수 계산
    teams = []

    for i in range(N):
        speed1, accuracy1, lang1, name1 = team_data[2 * i]
        speed2, accuracy2, lang2, name2 = team_data[2 * i + 1]

        score1 = compute_score(int(speed1), int(accuracy1), lang1)
        score2 = compute_score(int(speed2), int(accuracy2), lang2)

        avg_score = (score1 + score2) // 2
        A = str(avg_score)
        if len(A) == 2:
            A += '0'
        # 자리수 조합 생성
        avg_score_str = str(avg_score)  # 평균 점수를 문자열로 변환
        permuted_scores = permutations(avg_score_str)  # 모든 자리수 조합 생성
        permuted_scores2 = permutations(A)  # 모든 자리수 조합 생성
        possible_scores = set()  # 가능한 점수를 저장할 집합

        # 조합된 숫자들을 정수로 변환하여 집합에 추가
        for p in permuted_scores:
            score = int(''.join(p))  # 조합된 숫자를 정수로 변환
            possible_scores.add(score)  # 집합에 추가

        for p in permuted_scores2:
            score = int(''.join(p))  # 조합된 숫자를 정수로 변환
            possible_scores.add(score)  # 집합에 추가
        # minimum_difference 계산
        differences = []  # 차이를 저장할 빈 리스트 초기화
        for score in possible_scores:
            difference = abs(score - kang_score)  # 차이 계산
            differences.append(difference)  # 차이 저장

        minimum_difference = min(differences)  # 최소 차이를 찾음

        # best_score 찾기
        closest_scores = []  # minimum_difference와 동일한 차이를 가지는 점수를 저장할 리스트 초기화
        for score in possible_scores:
            if abs(score - kang_score) == minimum_difference:  # 조건 확인
                closest_scores.append(score)  # 조건을 만족하는 점수 저장

        best_score = max(closest_scores)  # 가장 큰 점수를 best_score에 저장

        teams.append((minimum_difference, best_score, name1, name2, avg_score, i))

    # 정렬: 점수 차 기준 오름차순, 점수 차가 같을 경우 원점수 기준 내림차순
    teams.sort(key=lambda x: (x[0], -x[4]))
    return teams


# 결과 출력 함수
def print_results(teams):
    for idx, (diff, score, name1, name2, avg, i) in enumerate(teams):
        print(f"{idx + 1}등 : {name1} {name2} ({i+1}팀) | 점수 차 : {diff} | 원점수 : {avg}")


# 팀 점수 계산 및 결과 출력
teams = calculate_team_scores(N, kang_s, kang_a, team_data)
print_results(teams)
