from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Language(TimeStampedModel):
    title = models.CharField(max_length=200)

class Letter(TimeStampedModel):
    title = models.CharField(max_length=200)

class Word(TimeStampedModel):
    title = models.CharField(max_length=200)

class Dictionary(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL , null=True, blank=True)
    words = models.ManyToManyField('Word', null=True, blank=True)


