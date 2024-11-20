from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from django.http.response import JsonResponse
from .models import Movie, Genre
import requests


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        "movies": movies,
        'genres': genres,
    }
    return render(request, "movies/index.html", context)


def filter_genre(request):
    genre = request.GET.get("genre")
    movies = list(Movie.objects.filter(genres__id=genre).values())
    context = {
        "movies": movies,
    }
    return JsonResponse(context)


@require_safe
def recommended(request):
    API_KEY = "9cbe77b703b0c172de8e80ade55ae511"
    CITY = "Seoul"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    main_weather = weather_data["weather"][0]["main"]

    if main_weather == "Rain":
        movies = Movie.objects.filter(genres__id=27)
    elif main_weather == "Snow":
        movies = Movie.objects.filter(genres__id=10749)
    elif main_weather == "Clear":
        movies = Movie.objects.filter(genres__id=12)
    elif main_weather == "Clouds":
        movies = Movie.objects.filter(genres__id=35)
    else:
        movies = Movie.objects.all()
    context = {
        "main_weather": main_weather,
        "movies": movies,
    }
    return render(request, "movies/recommended.html", context)
