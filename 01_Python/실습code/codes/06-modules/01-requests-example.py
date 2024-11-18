# 모듈 : 한 파일로 묶인 변수와 함수의 모음 /  특정한 기능을 하는 코드가 작성된 파이썬 파일
# 패키지 : 연관된 모듈들을 하나의 디렉토리에 모아 놓는 것


import requests

url = 'https://random-data-api.com/api/v2/users' # 랜덤 데이터 주소
response = requests.get(url).json()

print(response)