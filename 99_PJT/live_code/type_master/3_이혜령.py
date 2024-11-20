import sys
sys.stdin =open('real_input.txt',encoding='UTF8')

from itertools import permutations

# 학생 데이터 받아서 점수 계산하는 함수
def cal_score(ns, np, lan):
    if lan == "K":
        return int(ns*np//100*0.7)
    else:
        return ns*np//100

# 팀 수 N
N = int(input())

# 강사 점수 S, 강사 정확도 P
S, P = map(int, input().split())

# 학생정보 [[ns1, np1, lan1, name1], [ns2, np2, lan2, name2]], , , 으로 받기
student_lst = [[] for _ in range(N)]
for i in range(N*2):
    student_lst[i // 2].append(list(input().split()))

# 강사 점수 계산
t_score = S * P // 100

# 개인 별 점수 계산 후 평균, 점수차 구하고 저장
# 저장할 리스트
s_score_lst = []
# 인덱스 용
idx = -1
for students in student_lst:
    idx += 1
    s1 = students[0]
    s2 = students[1]
    s1_score = cal_score(int(s1[0]), int(s1[1]), s1[2])
    s2_score = cal_score(int(s2[0]), int(s2[1]), s2[2])

    s_score = (s1_score+s2_score)//2

    # 점수 2자리 수면 0 추가 그리고 순열 생성
    if s_score < 100:
        s_score = "0"+str(s_score)
    else:
        s_score = str(s_score)

    per_lst = list(permutations(s_score))

    # 강사님 점수와 차이가 가장 낮은 값이 이 팀의 최종 점수
    min_v = 10000
    for num in per_lst:
        score_gap = abs(t_score - int("".join(num)))
        if min_v > score_gap:
            min_v = score_gap

    # 정보 저장: 원래 인덱스, 점수 차, 원점수
    s_score_lst.append((idx, min_v, int("".join(s_score))))

# 정렬. 우선순위: 점수차(오름) -> 원점수(내림) -> 순서(오름)
s_score_lst.sort(key=lambda x: [x[1], -x[2], x[0]])

# 출력....
for i, result in enumerate(s_score_lst):
    print(f'{i+1}등 : {student_lst[result[0]][0][3]} {student_lst[result[0]][1][3]} ({result[0]+1} 팀) | ', end="")
    print(f'점수 차 : {result[1]} | 원점수 : {result[2]}')
