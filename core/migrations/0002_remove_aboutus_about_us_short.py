# Generated by Django 2.1.3 on 2018-11-25 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='about_us_short',
        ),
    ]
