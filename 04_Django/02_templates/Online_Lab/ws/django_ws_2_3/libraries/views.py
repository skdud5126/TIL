from django.shortcuts import render
import requests





# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbskdud51261424002'
    params = {
        'ttbkey': API_KEY,
        'QueryType' : 'ItemNewSpecial',
        'SearchTarget' : 'Book',
        'Output' : 'js',
        'Start' : 1,
        'MaxResults' : 50,
        'Version' : '20131101',
    }

    response = requests.get(API_URL, params= params).json()

    items = response.get('item')

    res = []
    dict_value = ['isbn','author', 'title', 'pubDate']
    dict_key = ['국제 표준 도서 번호', '저자', '제목', '출간일']
    for item in items:
        dict = {}
        for num in range(len(dict_value)):
            dict[dict_key[num]] = item.get(dict_value[num])
        res.append(dict)
    context = {
        'books' : res 
    }
    return render(request, 'recommend.html',context)