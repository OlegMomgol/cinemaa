from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm, DirectorForm, GenreForm


def movie_list(request):
    movies = Movie.objects.select_related("director", "genre").all()
    return render(request, "cinema/movie_list.html", {"movies": movies})


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request, "cinema/form.html", {"form": form, "title": "Добавить фильм"})


def add_director(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = DirectorForm()
    return render(request, "cinema/form.html", {"form": form, "title": "Добавить режиссёра"})


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = GenreForm()
    return render(request, "cinema/form.html", {"form": form, "title": "Добавить жанр"})