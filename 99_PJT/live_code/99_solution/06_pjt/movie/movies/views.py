from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Movie, Comment
from .form import MovieForm, CommentForm


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/create.html', context)


@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', pk)


@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', pk)
    context = {
        'comment_form': comment_form,
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)


@login_required
def likes(request, pk):
    movie = Movie.objects.get(pk=pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')


# 대댓글 생성
@login_required
def create_sub_comment(request, movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'POST':
        sub_comment_form = CommentForm(request.POST)
        if sub_comment_form.is_valid():
            sub_comment = sub_comment_form.save(commit=False)
            sub_comment.movie = movie
            sub_comment.user = request.user
            sub_comment.main_comment = comment
            sub_comment.save()
            return redirect('movies:detail', movie_pk)

    context = {
        'sub_comment_form': sub_comment_form,
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


# 대댓글 삭제
@login_required
def delete_sub_comment(request, movie_pk, comment_pk):
    sub_comment = Comment.objects.get(pk=comment_pk)
    if request.user == sub_comment.user:
        sub_comment.delete()
    return redirect('movies:detail', movie_pk)
