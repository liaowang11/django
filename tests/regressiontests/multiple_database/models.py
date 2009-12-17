from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models, DEFAULT_DB_ALIAS

class Review(models.Model):
    source = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return self.source

    class Meta:
        ordering = ('source',)

class Book(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateField()
    authors = models.ManyToManyField('Author')
    reviews = generic.GenericRelation(Review)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Author(models.Model):
    name = models.CharField(max_length=100)
    favourite_book = models.ForeignKey(Book, null=True, related_name='favourite_of')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)