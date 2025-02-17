# Generated by Django 4.2.16 on 2024-11-25 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('overview', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('poster_path', models.CharField(max_length=255)),
                ('genre1', models.CharField(blank=True, max_length=50)),
                ('genre2', models.CharField(blank=True, max_length=50)),
                ('genre3', models.CharField(blank=True, max_length=50)),
                ('actor1', models.CharField(blank=True, max_length=50)),
                ('actor2', models.CharField(blank=True, max_length=50)),
                ('actor3', models.CharField(blank=True, max_length=50)),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('wish_users', models.ManyToManyField(related_name='wish_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
