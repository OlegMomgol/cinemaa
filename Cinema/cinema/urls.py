from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("add/movie/", views.add_movie, name="add_movie"),
    path("add/director/", views.add_director, name="add_director"),
    path("add/genre/", views.add_genre, name="add_genre"),
]