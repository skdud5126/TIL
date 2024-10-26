from rest_framework import serializers
from .models import Article,Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # 기존 article 데이터 값을 override
    # 그런데 기존 필드를 override 하게되면 Meta클래스의 read_only_fields를 사용할 수 없음
    # 모델 시리얼라이저의 read_only 인자 값으로 재설정
    article = ArticleTitleSerializer(read_only=True)


    class Meta:
        model = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        fields = '__all__'
        # 외래 키 필드를 읽기전용 필드로 지정
        # 이유는?
        # 외래 키 데이터는
            # 1. 유효성 검사에서는 제외
            # 2. 결과 데이터에는 포함하고 싶음
        # read_only_fields = ('article',)