from django.db import models

class WordManager(models.Manager):
    def get_queryset(self):
        return super().get_query_set().filter()
