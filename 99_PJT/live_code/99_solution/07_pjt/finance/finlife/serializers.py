from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    # product 는 읽기 전용 필드로 지정한다.
    # product = serializers.ReadOnlyField(source='DepositOptions.product')
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product', )
