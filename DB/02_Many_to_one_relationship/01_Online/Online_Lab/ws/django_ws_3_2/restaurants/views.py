from django.shortcuts import render,redirect
from .models import Menu,Restaurant,Category
from .forms import CreateRestaurantForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    return render(request, 'restaurants/index.html',context)

def create_restaurant(request):
    if request.method == "POST":
        form = CreateRestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants:index')
    else:
        form = CreateRestaurantForm()
    context = {
        'form' : form, 
    }
    return render(request, 'restaurants/create.html',context)

def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant' : restaurant,
    }
    return render(request, 'restaurants/detail.html',context)