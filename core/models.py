from django.contrib.postgres.fields import ArrayField
from django.db import models


def upload_path(instance, filename):
    return "projects/{project_name}/{filename}".format(project_name=instance.title, filename=filename)


class Project(models.Model):
    title = models.CharField(verbose_name='name', max_length=300)
    thumbnail = models.ImageField(verbose_name='thumbnail', upload_to=upload_path)
    vimeo_url = models.URLField(verbose_name='vimeo url', null=True, blank=True, max_length=1000)
    short_description = models.CharField(verbose_name='short description', max_length=1000, null=True, blank=True)
    full_description = models.TextField(verbose_name='full description', null=True, blank=True)
    production_year = models.CharField(verbose_name='production year', max_length=10, null=True, blank=True)
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

    def __str__(self):
        return "First Page Projects"

    class Meta:
        verbose_name = 'First Page Projects'
        verbose_name_plural = 'First Page Projects'


class ContactUs(SingletonBaseModel):
    google_maps_src = models.URLField(verbose_name='google maps src', max_length=1000, null=True, blank=True)
    address = models.TextField(verbose_name='address', null=True, blank=True)
    telephones = ArrayField(models.CharField(max_length=30), null=True, blank=True, verbose_name='telephone numbers')
    faxes = ArrayField(models.CharField(max_length=30), null=True, blank=True, verbose_name='fax numbers')
    email = models.EmailField(verbose_name='email', null=True, blank=True)
    facebook = models.URLField(verbose_name='facebook url', null=True, blank=True, max_length=1000)
    twitter = models.URLField(verbose_name='twitter url', null=True, blank=True, max_length=1000)
    instagram = models.URLField(verbose_name='instagram', null=True, blank=True, max_length=1000)
    linkedin = models.URLField(verbose_name='linkedin url', null=True, blank=True, max_length=1000)
    youtube = models.URLField(verbose_name='youtube url', null=True, blank=True, max_length=1000)

    def __str__(self):
        return 'Contact Us'

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class SlideShowPicture(models.Model):
    image = models.ImageField(upload_to='slide_show/')

    def __str__(self):
        return 'image {filename}'.format(filename=self.image.name)


class Award(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    image = models.ImageField(upload_to='prizes/', null=True, blank=True)

    def __str__(self):
        return "award {title}".format(title=self.title)


class Founder(models.Model):
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', upload_to='founders/', null=True, blank=True)

    def __str__(self):
        return "founder {description}".format(description=self.description[:50])


class Artist(models.Model):
    name = models.CharField(max_length=500, verbose_name='name')
    image = models.ImageField(verbose_name='image', upload_to='artists/', null=True, blank=True)

    def __str__(self):
        return "artist {name}".format(name=self.name)


class Client(models.Model):
    homepage_url = models.URLField(verbose_name='homepage url', null=True, blank=True, max_length=1000)
    logo = models.ImageField(verbose_name='logo', upload_to='clients/')

    def __str__(self):
        return "client {logo}/{url}".format(logo=self.logo.name, url=self.homepage_url[:30])

class Service(models.Model):
    description = models.TextField(verbose_name='description', null=True, blank=True)
    image = models.ImageField(verbose_name='image', upload_to='services/', null=True, blank=True)

    def __str__(self):
        return "service {image}/{description}".format(image=self.image.name, description=self.description[:30])


class AboutUs(SingletonBaseModel):
    slide_show_pictures = models.ManyToManyField(SlideShowPicture, verbose_name='slide show pictures',
                                                 related_name='slide_show_pictures', blank=True)
    about_us_short = models.TextField(verbose_name='about us short description', null=True, blank=True)
    about_us_text = models.TextField(verbose_name='about us text', null=True, blank=True)
    aduren_reel_vimeo_url = models.URLField(verbose_name='Aduren Reel Vimeo URL', null=True, blank=True, max_length=1000)
    awards = models.ManyToManyField(Award, verbose_name='awards', related_name='awards', blank=True)
    founders = models.ManyToManyField(Founder, verbose_name='founders', related_name='founders', blank=True)
    artists = models.ManyToManyField(Artist, verbose_name='artists', related_name='artists', blank=True)
    clients = models.ManyToManyField(Client, verbose_name='clients', related_name='clients', blank=True)
    services = models.ManyToManyField(Service, verbose_name='services', related_name='services', blank=True)

    def __str__(self):
        return 'About Us'

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'
