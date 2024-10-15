import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbskdud51261424002'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)

def bestseller(request):
    params = {
        'TTBKey' : API_KEY,
        'QueryType' : 'Bestseller',
        'SearchTarget' : 'Book',
        'Start' : 1,
        'MaxResults' : 50,
        'Output' : 'JS',
        'Version' : '20131101',

    }

    response = requests.get(API_URL, params=params).json()
    items = response.get('item')

    res = []
    for item in items:
        if 'bestDuration' not in item:
            item['bestDuration'] = '설명 없음'
        dict = {
            '제목' : item['title'],
            '저자' : item['author'],
            '출간일' : item['pubDate'],
            '국제 표준 도서 번호(ISBN)' : item['isbn'],
            '판매 지수' : item['salesPoint'],
            '설명' : item['bestDuration'],
        }

        res.append(dict)


    context = {
        'items' : res,
    }
    return render(request, 'bestseller.html',context)