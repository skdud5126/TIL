from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def create(request):

    # 요청 메서드가 POST 일 때
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    # 요청 메서드가 POST가 아닐 때(GET, PUT, DELETE 등 다른 메서드)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')

# --------과거코드-----------#

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }

#     return render(request, 'articles/new.html', context)


# def create(request):
#     # 1. 모델폼 인스턴스 생성(+ 사용자 입력 데이터를 통째로 인자로 작성)
#     form = ArticleForm(request.POST)

#     # 2. 유효성 검사
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)

#     # 3. 저장

#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
    




# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)

#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):

#     article = Article.objects.get(pk=pk)
#     # 1. 모델폼 인스턴스 생성(+ 사용자 입력 데이터 & 기존 데이터 )
#     form = ArticleForm(request.POST, instance = article)
#     # 2. 유효성 검사
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)



    # # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # # 3. 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    # article.title = title
    # article.content = content
    # # 4. 저장
    # article.save()

    return redirect('articles:detail', article.pk)

