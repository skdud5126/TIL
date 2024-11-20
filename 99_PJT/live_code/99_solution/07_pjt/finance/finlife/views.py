import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# 1. 정기예금 상품 목록 DB에 저장
@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    baseList = response.get('result').get('baseList')   # 상품 목록
    optionList = response.get('result').get('optionList')    #  상품에 대한 옵션 목록 ( 하나의 상품에 여러 옵션이 존재 )
    
    for product in baseList:
        fin_prdt_cd = product.get('fin_prdt_cd')
        # 이미 추가된 데이터라면 생략
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue

        serializer = DepositProductsSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    
    # DepositOptions 의 product 필드가 DepositProducts 의 id 를 외래키로 참조하고 있기 때문에,
    # baseList 를 모두 저장한 후에 시행해야 한다. 
    for option in optionList:
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate')
        intr_rate2 = option.get('intr_rate2')

        save_trm = option.get('save_trm')

        # 어떤 상품의 옵션인지 검색
        deposit_product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)[0]
        # 이미 추가된 데이터라면 생략
        if DepositOptions.objects.filter(product=deposit_product.id,
                                         intr_rate_type_nm=intr_rate_type_nm,
                                         save_trm=save_trm,
                                         intr_rate=intr_rate,
                                         intr_rate2=intr_rate2).exists():
            continue

        # pro = {
        #     'product': deposit_product.id,
        #     'fin_prdt_cd': deposit_product.fin_prdt_cd,
        #     'intr_rate_type_nm': option.get('intr_rate_type_nm'),
        #     'intr_rate': option.get('intr_rate') if option.get('intr_rate') is not None else -1,
        #     'intr_rate2': option.get('intr_rate2') if option.get('intr_rate2') is not None else -1,
        #     'save_trm': option.get('save_trm'),
        # }

        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=deposit_product)
    
    return Response({ 'message': 'okay '})

# 2. 전체 정기예금 상품 목록 출력
# 5. 데이터 삽입
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({ 'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'})
    
    products = DepositProducts.objects.all()
    # many=True - Qureyset 에 리스트를 허용하기 위한 옵션
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)

# 3. 특정 상품의 옵션 리스트 출력
# 특정 상품 데이터 반환 (금융 상품 코드로 조회)
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    options = DepositOptions.objects.filter(product__exact=product.id)
    # many=True - Qureyset 에 리스트를 허용하기 위한 옵션
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

# 4. 특정 조건의 상품 + 옵션 출력
# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate(request):
    # 금리 역순 정렬의 가장 맨 앞(금리가 가장 높은 옵션)
    top_rate_option = DepositOptions.objects.all().order_by('-intr_rate2').first()

    # 위에서 구한 옵션의 외래키를 이용하여 예금 상품 정보를 가져옴
    top_product_id = top_rate_option.product
    deposit_product = DepositProducts.objects.filter(id=top_product_id.id).first()
    
    # 위에서 구한 옵션의 외래키를 이용하여 같은 외래키의 옵션 데이터들을 가져옴
    top_product_options = DepositOptions.objects.filter(product=top_product_id)

    # 위 데이터들을 함께 반환
    context = {
        'deposit_product': DepositProductsSerializer(deposit_product).data,
        'options': DepositOptionsSerializer(top_product_options, many=True).data
    }
    return Response(context)
