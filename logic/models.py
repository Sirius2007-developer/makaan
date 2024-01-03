from django.db import models
from django.urls import reverse


# Create your models here.
class Carousel(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    bio = models.TextField()
    location = models.TextField()
    sqft = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("listdetail", args=[self.slug])

    def __str__(self):
        return self.name


class List1(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    bio = models.TextField()
    location = models.TextField()
    sqft = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("teamdetail", args=[self.slug])

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    comment = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name