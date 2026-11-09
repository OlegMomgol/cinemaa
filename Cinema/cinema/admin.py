from django.contrib import admin
from .models import Director, Genre, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "rating", "duration_minutes", "director", "genre")
    list_filter = ("genre", "year")
    search_fields = ("title", "director__name")
    list_select_related = ("director", "genre")