import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'alice', 
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

# def catch(request):
#     # 사용자가 요청보낸 데이터를 추출해서 context 딕셔너리에 세팅
#     context = {
#         'message' : 
#     }
#     return render(request, 'article/throw.html')