# articles/models.py
from django.db import models
from accounts.models import User
from django.conf import settings

# Create your models here.
# Article (N) : User(1)
class Article(models.Model):
    # user에 대한 정보 외래키로 설정
    # 일반적인 다른 app으로부터 Model을 import 받아왔을 때 발생하는 문제
    # settings.py -> INSTALLED_APPS에 등록한 순서에 영향을 받는다.
    # 현재 활성화 된 User 모델이 무엇인지는 settings.py에 이미 써놨었따.
        # AUTH_USER_MODEL = 'accounts.User' 라는 모델을 문자열로 적어둠.
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete
    # CASCADE => 내 참조 대상이 DB에서 사라졌을 떄, 나도 함께 삭제
    # 지금은 django 연습 중 => 항상 CASCADE => 제일 안귀찮음

    # article = models.ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을때)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)