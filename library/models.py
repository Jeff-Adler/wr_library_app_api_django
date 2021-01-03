from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['title']


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['last_name', 'first_name']
