# Generated by Django 4.2.5 on 2023-09-20 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movie_movie_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="movie_image",
        ),
    ]