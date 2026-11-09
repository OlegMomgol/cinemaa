from django import forms
from .models import Director, Genre, Movie


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ["name", "country"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "year", "rating", "duration_minutes", "director", "genre"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "duration_minutes": forms.NumberInput(attrs={"class": "form-control"}),
            "director": forms.Select(attrs={"class": "form-select"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
        }