from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    country = models.CharField(max_length=100, verbose_name="Страна")

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год")
    rating = models.IntegerField(verbose_name="Рейтинг")
    duration_minutes = models.IntegerField(verbose_name="Длительность (мин)")
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies",
        verbose_name="Режиссёр",
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="movies",
        verbose_name="Жанр",
    )

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["-year"]

    def __str__(self):
        return f"{self.title} ({self.year}) – {self.director.name}"