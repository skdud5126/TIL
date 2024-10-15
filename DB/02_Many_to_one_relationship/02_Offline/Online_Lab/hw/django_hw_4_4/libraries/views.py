from django.shortcuts import render,redirect
from .models import Book,Review
from .forms import CreateReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    review_form = CreateReviewForm()
    context = {
        'book': book,
        'review_form' : review_form,
        'reviews' : reviews,
    }
    return render(request, 'libraries/detail.html', context)

def create_review(request, book_pk):
    book = Book.objects.get(pk = book_pk)
    review_form = CreateReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit = False)
        review.user = request.user
        review.book = book
        review.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'book' : book,
        'review_form' : review_form,
    }
    return render('libraries:detail',context)