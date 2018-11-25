from django.contrib.postgres.fields import ArrayField
from django.db import models


def upload_path(instance, filename):
    return "{project_name}/{filename}".format(project_name=instance.title, filename=filename)


class Project(models.Model):
    title = models.CharField(verbose_name='name', max_length=300)
    thumbnail = models.ImageField(verbose_name='thumbnail', upload_to=upload_path)
    vimeo_url = models.URLField(verbose_name='vimeo url', null=True, blank=True)
    short_description = models.CharField(verbose_name='short description', max_length=1000, null=True, blank=True)
    full_description = models.TextField(verbose_name='full description', null=True, blank=True)
    production_year = models.CharField(verbose_name='production year', max_length=10)
    image = models.ImageField(verbose_name='image', upload_to=upload_path)

    def __str__(self):
        return 'project {title}'.format(title=self.title)


class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class FirstPageProjects(SingletonBaseModel):
    projects = models.ManyToManyField(Project, related_name='first_page_projects')

    class Meta:
        verbose_name = 'First Page Projects'
        verbose_name_plural = 'First Page Projects'


class ContactUs(SingletonBaseModel):
    google_maps_embed_html = models.TextField(verbose_name='google maps embeded html')
    address = models.TextField(verbose_name='address')
    telephones = ArrayField(models.CharField(max_length=30), null=True, blank=True, verbose_name='telephone numbers')
    faxes = ArrayField(models.CharField(max_length=30), null=True, blank=True, verbose_name='fax numbers')
    facebook = models.URLField(verbose_name='facebook url', null=True, blank=True)
    twitter = models.URLField(verbose_name='twitter url', null=True, blank=True)
    instagram = models.URLField(verbose_name='instagram', null=True, blank=True)
    linkedin = models.URLField(verbose_name='linkedin url', null=True, blank=True)
    youtube = models.URLField(verbose_name='youtube url', null=True, blank=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class SlideShowPicture(models.Model):
    image = models.ImageField(upload_to='slide_show/')

    def __str__(self):
        return 'image {filename}'.format(filename=self.image.name)


class Prize(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    image = models.ImageField(upload_to='prizes/')


class Founder(models.Model):
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', upload_to='founders/')


class Artist(models.Model):
    name = models.CharField(max_length=500, verbose_name='name')
    image = models.ImageField(verbose_name='image', upload_to='artists/')


class Client(models.Model):
    homepage_url = models.URLField(verbose_name='homepage url', null=True, blank=True)
    logo = models.ImageField(verbose_name='logo', upload_to='clients/')


class Service(models.Model):
    description = models.TextField(verbose_name='description', null=True, blank=True)
    image = models.ImageField(verbose_name='image', upload_to='services/')


class AboutUs(SingletonBaseModel):
    slide_show_pictures = models.ManyToManyField(SlideShowPicture, verbose_name='slide show pictures',
                                                 related_name='slide_show_pictures')
    about_us_text = models.TextField(verbose_name='about us text')
    aduren_reel_vimeo_url = models.URLField(verbose_name='Aduren Reel Vimeo URL')
    prizes = models.ManyToManyField(Prize, verbose_name='prizes', related_name='prizes')
    founders = models.ManyToManyField(Founder, verbose_name='founders', related_name='founders')
    artists = models.ManyToManyField(Artist, verbose_name='artists', related_name='artists')
    clients = models.ManyToManyField(Client, verbose_name='clients', related_name='clients')
    services = models.ManyToManyField(Service, verbose_name='services', related_name='services')

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'
