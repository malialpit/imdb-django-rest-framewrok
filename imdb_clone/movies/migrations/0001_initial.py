# Generated by Django 3.2.8 on 2021-10-27 14:59

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=5, help_text='The number of extra random characters be suffixed \n        to slug if needed. default is 0 and it means no extra chars.', validators=[django.core.validators.MaxValueValidator(9, message='max value is 9')], verbose_name='extra characters count')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='title')),
                ('original_name', models.CharField(blank=True, default='', max_length=245, verbose_name='original title')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='release date')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, help_text='in minutes', verbose_name='duration')),
                ('imdb_rating', models.FloatField(blank=True, default=0, help_text='e.g. 6.8', validators=[django.core.validators.MinValueValidator(0.0, message='min. value cannot be negative'), django.core.validators.MaxValueValidator(10.0, message='max. value cannot be more then 10')], verbose_name='IMDB rating')),
                ('imdb_raters_count', models.PositiveIntegerField(blank=True, default=0, verbose_name='IMDB raters count')),
                ('imdb_id', models.CharField(blank=True, db_index=True, default='', max_length=15, verbose_name='IMDB Id')),
                ('intro', models.TextField(blank=True, default='', max_length=500, verbose_name='intro')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='content')),
                ('content_source', models.URLField(blank=True, default='', verbose_name='content source')),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (ONLY for youtube videos yet)', verbose_name='trailer')),
                ('trailer_info', models.CharField(blank=True, default='', max_length=250, verbose_name='trailer info')),
                ('country', models.CharField(blank=True, default='', max_length=100, verbose_name='country')),
                ('language', models.CharField(blank=True, default='', max_length=100, verbose_name='language')),
                ('image', models.ImageField(blank=True, null=True, upload_to=movies.models.movie_directory_path, verbose_name='image')),
                ('image_credit', models.CharField(blank=True, default='', max_length=250, verbose_name='image credit')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
            },
        ),
    ]
