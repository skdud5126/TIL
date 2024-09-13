import os
import subprocess

curent_folder = os.getcwd()  # 현재 작업 영역 경로 확인
print(curent_folder)

'''
https://lab.ssafy.com/skdud5126/django_hw_1_2
코드를 쓴다 -> 반복문을 쓸 수 있다.
똑같은 일을 반복해서 시킬 수 있다.

'''

USER_NAME = 'skdud5126'
SUBJECT = input('과목을 입력해 주세요. ex) django, db, js, vue : ')
SEPERATOR = 'hw'
DAY = input('날짜를 입력해 주세요. : ')
# STAGE = '2'

for sep in ['hw', 'ws']:
    # 만약, sep - > hw이면 2, 4만 순회
    # 만약, sep - > wsdlaus 1 ~ c 까지 순회
    for stage in [1, 2, 3, 4, 5, 'a', 'b', 'c']:
        BASE_URL = f'https://lab.ssafy.com/{USER_NAME}/{SUBJECT}_{sep}_{DAY}_{stage}'
        subprocess.run(['git', 'clone', BASE_URL])

# print(BASE_URL)


