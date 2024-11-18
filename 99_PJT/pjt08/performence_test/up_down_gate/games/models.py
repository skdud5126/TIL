from django.db import models

# Create your models here.
class GameSession(models.Model):
    # 정답
    target_number = models.IntegerField()
    # 사용자의 추측
    user_guess = models.IntegerField(null=True)
    # 추측 횟수
    attempts = models.IntegerField(default=0)
    