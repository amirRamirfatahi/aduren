# Generated by Django 2.1.3 on 2018-11-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contactus_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='google_maps_src',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='google maps src'),
        ),
    ]