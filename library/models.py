from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    # books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = [['first_name', 'last_name']]

    def __str__(self):
        return '%d: %s %s' % (self.id, self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(
        max_length=100, blank=True, default='', unique=True)
    authors = models.ManyToManyField(Author, related_name="book_list")

    class Meta:
        ordering = ['title']


class Alt(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    book = models.ForeignKey(Book,
                             on_delete=models.RESTRICT,
                             related_name='alts'
                             )

    class Meta:
        ordering = ['title']
