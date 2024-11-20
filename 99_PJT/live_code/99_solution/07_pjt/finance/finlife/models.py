from django.db import models


# 정기예금 상품 리스트
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품 코드
    kor_co_nm = models.TextField()  # 금융회사명
    fin_prdt_nm = models.TextField()  # 상품명
    etc_note = models.TextField()  # 상품설명
    join_deny = (
        models.IntegerField()
    )  # 가입제한 (1: 제한없음, 2: 서민전용, 3: 일부제한)
    join_member = models.CharField(
        max_length=200
    )  # 가입대상 ex) 실명의 개인, 제한없음, 만 50세 이상 등
    join_way = models.CharField(
        max_length=300
    )  # 가입 방법 ex) 영업점, 인터넷, 스마트폰 등
    spcl_cnd = models.TextField()  # 우대조건


# 예금 상품의 옵션 리스트
class DepositOptions(models.Model):
    product = models.ForeignKey(
        DepositProducts,
        on_delete=models.CASCADE,
        related_name='deposit_options',
    )
    fin_prdt_cd = models.TextField()  # 금융상품 코드
    intr_rate_type_nm = models.CharField(
        max_length=50
    )  # 저축금리 유형명 ex) 단리, 복리
    intr_rate = models.FloatField(null=True)  # 저축금리
    intr_rate2 = models.FloatField(null=True)  # 최고우대금리
    save_trm = models.IntegerField()  # 저축기간 [단위: 개월]
