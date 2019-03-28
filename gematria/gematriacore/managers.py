from django.db import models

class WordManager(models.Manager):
    def get_queryset(self):
        word = super().get_queryset().filter()
        return word.
