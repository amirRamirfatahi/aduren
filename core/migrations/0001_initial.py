# Generated by Django 2.1.3 on 2018-11-25 17:44

import core.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_short', models.TextField(blank=True, null=True, verbose_name='about us short description')),
                ('about_us_text', models.TextField(blank=True, null=True, verbose_name='about us text')),
                ('aduren_reel_vimeo_url', models.URLField(blank=True, max_length=1000, null=True, verbose_name='Aduren Reel Vimeo URL')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='artists/', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='prizes/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_url', models.URLField(blank=True, max_length=1000, null=True, verbose_name='homepage url')),
                ('logo', models.ImageField(upload_to='clients/', verbose_name='logo')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_maps_src', models.URLField(blank=True, max_length=1000, null=True, verbose_name='google maps src')),
                ('address', models.TextField(blank=True, null=True, verbose_name='address')),
                ('telephones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None, verbose_name='telephone numbers')),
                ('faxes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None, verbose_name='fax numbers')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('facebook', models.URLField(blank=True, max_length=1000, null=True, verbose_name='facebook url')),
                ('twitter', models.URLField(blank=True, max_length=1000, null=True, verbose_name='twitter url')),
                ('instagram', models.URLField(blank=True, max_length=1000, null=True, verbose_name='instagram')),
                ('linkedin', models.URLField(blank=True, max_length=1000, null=True, verbose_name='linkedin url')),
                ('youtube', models.URLField(blank=True, max_length=1000, null=True, verbose_name='youtube url')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='FirstPageProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'First Page Projects',
                'verbose_name_plural': 'First Page Projects',
            },
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='founders/', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='name')),
                ('thumbnail', models.ImageField(upload_to=core.models.upload_path, verbose_name='thumbnail')),
                ('vimeo_url', models.URLField(blank=True, max_length=1000, null=True, verbose_name='vimeo url')),
                ('short_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='short description')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='full description')),
                ('production_year', models.CharField(blank=True, max_length=10, null=True, verbose_name='production year')),
                ('image', models.ImageField(upload_to=core.models.upload_path, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='SlideShowPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_show/')),
            ],
        ),
        migrations.AddField(
            model_name='firstpageprojects',
            name='projects',
            field=models.ManyToManyField(related_name='first_page_projects', to='core.Project'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='artists', to='core.Artist', verbose_name='artists'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='awards', to='core.Award', verbose_name='awards'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='clients', to='core.Client', verbose_name='clients'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='founders',
            field=models.ManyToManyField(blank=True, related_name='founders', to='core.Founder', verbose_name='founders'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='services', to='core.Service', verbose_name='services'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='slide_show_pictures',
            field=models.ManyToManyField(blank=True, related_name='slide_show_pictures', to='core.SlideShowPicture', verbose_name='slide show pictures'),
        ),
    ]