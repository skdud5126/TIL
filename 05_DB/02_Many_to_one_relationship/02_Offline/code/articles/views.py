from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_http_methods, require_POST

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

# POST 요청과 GET요청만 허용
# require_http_methods 데코레이터가 없는 상황에서
# PUT/PATHC, DELETE 등의 메서드등의 요청이 들어오게 되면?
# 로직상, if문으로 POST에 대해서만 조건분기를 해뒀고,
# 나머지(else) 그냥 HTML 반환하는 형식으로 코드를 작성해 놨다.


@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 게시글 생성을 위해, 넘겨받은 데이터로 생성할 건데
            # 사용자가 넘겨준 데이터에는 user에 대한 정보는 from에 없다.
            # 그래서 일단, 객체를 만들긴 할건데..
                # DB에 반영은 하지 말아봐
            article = form.save(commit=False)
            # DB에 반영되지 않았지만... 사용자가 form으로 보낸
            # title, content를 포함한 article객체가 만들어졌고,
            # 그 article 객체는 ArticleForm으로 만들어 졌으니,
                # class Meta의 model = Article을 적어 놨기 때문에
            # 내가 만든 models의 Article class의 인스턴스가 되겠다.
            # 그래서 article.user정보에 요청보낸 user의 정보를 담는다.
            article.user = request.user
            article = form.save() # DB에 반영
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # 아무리 작성자라도.. POST 요청일때만 ... 삭제 할 수 있어야 할 것 같은데
    # if request.method == 'POST'
    # 작성자만 게시글을 삭제할 수 있는 상태
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
def update(request, pk):
    # 이미 게시글과 User의 1:N 관계에 대한 정의는
    # model과 Form, 그리고 CREATE 로직에서 다 처리했음.
    # update는 수정할 일 없음!
    article = Article.objects.get(pk=pk)
    # 단, 작성자 본인인 경우에만 수정할 수 있어야함.
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # 작성자 정보만 추가
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
