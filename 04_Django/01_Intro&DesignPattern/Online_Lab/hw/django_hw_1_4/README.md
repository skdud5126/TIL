# django 시작하기

```bash
# 1. 프로젝트 시작하자마자 gitignore 생성하기
$ code .gitignore

# 2. 
$ python -m venv venv

# 3. 가상환경 활성화 하기
$ source venv/Scripts/Activate

# 4. 프로젝트 진행에 필요한 라이브러리 설치하기
$ pip install django

    # pip list로 설치 라이브러리 상황 확인하기 (습관!!)

# 5. 현재 버전을 다음에도 똑같이 유지하기 위해 기록
$ pip freeze > requirements.txt
```
2. django 프로젝트 생성하기

```bash
# 장고야 프로젝트 시작해줘 my_pjt를 현재 폴더에.
$ django-admin startproject my_pjt .

# 1. 서버 키기
$ python manage.py runserver

# 2. 서버끄기
ctrl + c
```

---

3. 앱 생성 및 등록

```bash
# 가능하지만 안씀
# $ djang-admin startapp my_app

# 1. 앱 생성 -> 등록
$ python manage.py startapp my_app
```

> 프로젝트는 프로젝트 생성 명령어로 만듦
  - 이 때, app은 없었음.

> 그러고 나서, 추가로 app을 생성했음.
  - 이건.. 프로젝트랑 완전 별개 폴더(패키지)이다.

> 프로젝트가 방금 만들어진 app의 존재를 알