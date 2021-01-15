from django.db import models

#comment made with the express purpose of keeping my github green
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = [['first_name', 'last_name']]

    def __str__(self):
        return '%d: %s %s' % (self.id, self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(
        max_length=100, unique=True)
    authors = models.ManyToManyField(
        Author, related_name="book_list", blank=True)

    class Meta:
        ordering = ['title']


class Alt(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book,
                             default='',
                             on_delete=models.RESTRICT,
                             related_name='alts'
                             )

    class Meta:
        ordering = ['title']
