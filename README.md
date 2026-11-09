Кинотеатр
Каталог фильмов с режиссёрами и жанрами.

- Python 3.10+
- Django 5.x
- SQLite
- Bootstrap 5 (CDN)
Возможности:
- Модели: Director, Genre, Movie (ForeignKey + CASCADE/PROTECT).
- Формы добавления фильмов, режиссёров и жанров.
- Список фильмов в формате «Название (год) – режиссёр».
- Админка: list_display, list_filter по жанрам и годам, search_fields.
- select_related для оптимизации запросов.

Установка и запуск:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
