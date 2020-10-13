from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Casmena')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='tba')
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

#TODO pip install django-ckeditor

